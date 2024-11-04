from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.chat_history import ChatHistoryCreate
from core.services.chat_history import ChatHistoryService, provide_chat_history_service


async def create_chat_history(session: AsyncSession, data: ChatHistoryCreate) -> None:
    chat_history_service: ChatHistoryService = provide_chat_history_service(session)
    await chat_history_service.create(data)
