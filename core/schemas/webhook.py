from typing import Optional

from core.schemas.base import BaseSchema


class WebhookIn(BaseSchema):
    message: str
    # callback_url: Optional[str] = None


class Message(BaseSchema):
    content: str


class Choice(BaseSchema):
    message: Message


class ChatResponse(BaseSchema):
    id: str
    created: int
    choices: list[Choice]
