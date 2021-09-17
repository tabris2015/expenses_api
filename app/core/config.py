import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Expense manager"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = "postgresql://user:password@localhost/fastapi" #"sqlite:///database.db"

    class Config:
        env_file = ".env"


settings = Settings()
