from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from remember_me_backend.api.dependencies import AsyncSessionDep, CurrentUserDep
from remember_me_backend.services import chat_session as chat_session_service


class ChatSessionBase(BaseModel):
    title: str | None = None
    description: str | None = None

    updated_at: datetime
    created_at: datetime


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSession(ChatSessionBase):
    id: int
    transcript: str | None = None
    summary: str | None = None

    class Config:
        from_attributes = True


router = APIRouter()


@router.post("/create", response_model=ChatSession)
async def create_chat_session(
    user: CurrentUserDep,
    session: AsyncSessionDep,
    title: str | None = None,
    description: str | None = None,
):
    chat_session = await chat_session_service.create_chat_session(
        session=session,
        title=title,
        description=description,
        user=user,
    )
    return chat_session


@router.get("/{chat_session_uuid}", response_model=ChatSession)
async def get_chat_session(
    chat_session_uuid: int,
    user: CurrentUserDep,
    session: AsyncSessionDep,
):
    return await chat_session_service.get_chat_session(
        session=session, chat_session_id=chat_session_uuid, user=user
    )
