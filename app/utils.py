
from datetime import datetime
import functools
import logging
from .config import settings
from fastapi_mail import ConnectionConfig


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

mail_conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_PORT=465,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

def log_on_completion(task_func):
    @functools.wraps(task_func)
    async def wrapper(*args, **kwargs):
        result = await task_func(*args, **kwargs)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Task '{task_func.__name__}' successfully executed at: {now}")
        return result
    return wrapper



