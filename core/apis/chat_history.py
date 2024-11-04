from typing import Annotated, List

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.helper import db
from core.config import settings

from core.schemas.chat_history import ChatHistoryRetrieve, ChatHistoryUpdate
from core.services.chat_history import ChatHistoryService, provide_chat_history_service

router = APIRouter(tags=[settings.tags.chat_history])


@router.get("/", response_model=List[ChatHistoryRetrieve])
async def get_all(
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    service: ChatHistoryService = provide_chat_history_service(session)
    return await service.list()


@router.patch("/update/{id}")
async def update(
    id: int,
    session: Annotated[AsyncSession, Depends(db.get_session)],
    data: ChatHistoryUpdate,
):
    service: ChatHistoryService = provide_chat_history_service(session)
    return await service.update(id, data)


@router.delete("/delete/{id}", status_code=204)
async def delete(
    id: int,
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    service: ChatHistoryService = provide_chat_history_service(session)
    await service.delete(id)
