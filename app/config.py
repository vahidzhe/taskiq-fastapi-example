from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class AppSettings(BaseSettings):

    
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_FROM_NAME: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_SSL_TLS: bool
    REDIS_URL: str
    
    
    
@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


settings = get_app_settings()


