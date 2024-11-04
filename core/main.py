from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from core.routers import router

from core.db.helper import db

from core.utils.logging_config import log_queue_listener_service
from core.middlewares.logging_middleware import APIRequestLoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # StartUp
    log_queue_listener_service.start()
    yield
    # ShutDown
    log_queue_listener_service.stop()
    await db.dispose()


app = FastAPI(title="ON-AI", lifespan=lifespan)

app.add_middleware(APIRequestLoggingMiddleware)

app.include_router(router, prefix=settings.prefix.api)
