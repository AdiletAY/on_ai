import logging
from logging.handlers import RotatingFileHandler
from queue import SimpleQueue

from core.config import settings

log_queue = SimpleQueue()


log_queue_handler = logging.handlers.QueueHandler(log_queue)


log_message_formatter = logging.Formatter(
    fmt=(
        "TIME (%(asctime)s) - %(levelname)s - %(message)s - "
        "SERVICE: %(service)s - METHOD: %(method)s - "
        "STATUS: %(status_code)s - TIME: %(time)s seconds"
    )
)

log_file_handler_with_rotation = RotatingFileHandler(
    f"./logs/{settings.logging.file_name}.log",
    maxBytes=settings.logging.file_size,
    backupCount=settings.logging.file_backup_count,
)
log_file_handler_with_rotation.setFormatter(log_message_formatter)

log_queue_listener_service = logging.handlers.QueueListener(
    log_queue,
    log_file_handler_with_rotation,
)

api_response_logger = logging.getLogger("APIResponseLogger")
api_response_logger.addHandler(log_queue_handler)
api_response_logger.setLevel(logging.INFO)
