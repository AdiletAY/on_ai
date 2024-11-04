from core.repositories.base import BaseRepository

from core.models.chat_history import ChatHistoryModel
from core.schemas.chat_history import ChatHistoryCreate, ChatHistoryUpdate


class ChatHistoryRepository(
    BaseRepository[
        ChatHistoryModel,
        ChatHistoryCreate,
        ChatHistoryUpdate,
    ]
):
    def __init__(self, model, session):
        super().__init__(model, session)
