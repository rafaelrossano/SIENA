import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str = os.getenv("SQLITE_DATABASE_URL", "")
    TOKEN_SECRET_KEY: str = os.getenv("TOKEN_SECRET_KEY", "")
    TOKEN_ALGORITHM: str = os.getenv("TOKEN_ALGORITHM", "HS256")
    TOKEN_EXPIRE_MINUTES: str = os.getenv("TOKEN_EXPIRE_MINUTES", '30')

settings = Settings()