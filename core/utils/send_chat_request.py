import json
import requests

from core.config import settings
from core.schemas.webhook import ChatResponse

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def send_chat_request(message: str, callback_url: str = OPENROUTER_URL) -> ChatResponse:
    headers = {
        "Authorization": f"Bearer {settings.openrouter.api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": settings.openrouter.model,
        "messages": [
            {
                "role": "user",
                "content": message,
            }
        ],
    }

    response = requests.post(
        url=callback_url,
        headers=headers,
        data=json.dumps(payload),
    )
    response_data = response.json()

    return ChatResponse(**response_data)
