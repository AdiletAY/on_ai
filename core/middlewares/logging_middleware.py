import time
import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class APIRequestLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)

        logging.getLogger("APIResponseLogger").info(
            "Successfully called API",
            extra={
                # "username": await self.get_username(request),
                "status_code": response.status_code,
                "service": str(request.url),
                "method": request.method,
                "time": process_time,
            },
        )
        return response
