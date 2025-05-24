from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str = os.getenv("SQLITE_DATABASE_URL", "")

    TOKEN_SECRET_KEY: str = os.getenv("TOKEN_SECRET_KEY", "")
    TOKEN_ALGORITHM: str = os.getenv("TOKEN_ALGORITHM", "")
    TOKEN_EXPIRE_MINUTES: str = os.getenv("TOKEN_EXPIRE_MINUTES", "")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()