from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from remember_me_backend.api.dependencies import CurrentUserDep, SyncSessionDep
from remember_me_backend.services import chat_session


class ChatSessionBase(BaseModel):
    title: str | None = None
    description: str | None = None


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSession(ChatSessionBase):
    id: int
    transcript: str | None = None
    summary: str | None = None

    class Config:
        from_attributes = True


router = APIRouter()


@router.post("/", response_model=ChatSession)
async def create_session(
    user: CurrentUserDep,
    session: SyncSessionDep,
    title: str | None = None,
    description: str | None = None,
):
    return await chat_session.create_session(
        session=session,
        title=title,
        description=description,
        user=user,
    )


@router.get("/{session_uuid}", response_model=ChatSession)
async def get_session(
    session_id: int,
    user: CurrentUserDep,
    session: SyncSessionDep,
):
    return await chat_session.get_session(
        session=session, session_id=session_id, user=user
    )
