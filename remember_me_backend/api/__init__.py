from fastapi import APIRouter
from remember_me_backend.api import router_chat_sessions

router = APIRouter()

router.include_router(router_chat_sessions.router, prefix="/chatsessions", tags=["chatsessions"])
