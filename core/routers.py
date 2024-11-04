from fastapi import APIRouter

from core.config import settings
from core.apis.webhook import router as webhook_router
from core.apis.chat_history import router as chat_history_router

router = APIRouter()
router.include_router(webhook_router, prefix=settings.prefix.webhook)
router.include_router(chat_history_router, prefix=settings.prefix.chat_history)
