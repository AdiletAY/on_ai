from typing import Optional
from core.schemas.base import BaseSchema


class ChatHistoryCreate(BaseSchema):
    message: str
    created: int


class ChatHistoryUpdate(BaseSchema):
    message: Optional[str] = None
    created: Optional[int] = None


class ChatHistoryRetrieve(BaseSchema):
    id: int
    message: str
    created: int
