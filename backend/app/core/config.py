import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    SQLITE_DATABASE_URL: str = os.getenv("SQLITE_DATABASE_URL", "")

settings = Settings()