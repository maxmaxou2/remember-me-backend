from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Remember Me API"
    VERSION: str = "0.1.0"
    ROUTER_PREFIX: str = "/api/v1"

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    # Database
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:yourpassword@localhost:5432/remember_me_backend"
    )

    class Config:
        case_sensitive = True


settings = Settings()
