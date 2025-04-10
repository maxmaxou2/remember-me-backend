from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Remember Me API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]  # Add your frontend URL

    # Database
    DATABASE_URL: str = "sqlite:///./remember_me.db"

    # JWT
    JWT_SECRET: str = "your-secret-key"  # Change this!
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    class Config:
        case_sensitive = True


settings = Settings()
