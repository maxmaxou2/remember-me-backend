from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from remember_me_backend.api import router as api_router
from remember_me_backend.core.config import settings


def make_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)
    return app


app = make_app()
