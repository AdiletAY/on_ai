from typing import Annotated

from fastapi import APIRouter, Depends, BackgroundTasks

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.helper import db
from core.config import settings
from core.schemas.webhook import ChatResponse, WebhookIn
from core.schemas.chat_history import ChatHistoryCreate
from core.utils.send_chat_request import send_chat_request
from core.utils.create_chat_history import create_chat_history

router = APIRouter(tags=[str(settings.tags.webhook)])


@router.post("/", response_model=ChatResponse)
async def webhook(
    background_tasks: BackgroundTasks,
    session: Annotated[AsyncSession, Depends(db.get_session)],
    data: WebhookIn = Depends(),
):
    chat_response = send_chat_request(
        message=data.message,
        # callback_url=data.callback_url,
    )
    background_tasks.add_task(
        create_chat_history,
        session,
        ChatHistoryCreate(
            message=chat_response.choices[0].message.content,
            created=chat_response.created,
        ),
    )
    return chat_response
