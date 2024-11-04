from sqlalchemy.ext.asyncio import AsyncSession


from core.services.base import BaseServiceInt
from core.models.chat_history import ChatHistoryModel
from core.repositories.chat_history import ChatHistoryRepository
from core.schemas.chat_history import ChatHistoryCreate, ChatHistoryUpdate


class ChatHistoryService(
    BaseServiceInt[
        ChatHistoryModel,
        ChatHistoryRepository,
        ChatHistoryCreate,
        ChatHistoryUpdate,
    ]
):
    def __init__(self, repository: ChatHistoryRepository) -> None:
        super().__init__(repository)


def provide_chat_history_service(session: AsyncSession) -> ChatHistoryService:
    repository: ChatHistoryRepository = ChatHistoryRepository(ChatHistoryModel, session)
    return ChatHistoryService(repository)
