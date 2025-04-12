from fastapi import APIRouter
from pydantic import BaseModel

from remember_me_backend.api.dependencies import AsyncSessionDep, CurrentUserDep
from remember_me_backend.services import chat_session as chat_session_service


class ChatSessionBase(BaseModel):
    title: str | None = None
    description: str | None = None


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSession(ChatSessionBase):
    id: int
    # transcript: str | None = None
    # summary: str | None = None

    class Config:
        from_attributes = True
        orm_mode = True


router = APIRouter()


@router.post("/", response_model=ChatSession)
async def create_session(
    user: CurrentUserDep,
    session: AsyncSessionDep,
    title: str | None = None,
    description: str | None = None,
):
    chat_session = await chat_session_service.create_session(
        session=session,
        title=title,
        description=description,
        user=user,
    )
    return chat_session


@router.get("/{session_uuid}", response_model=ChatSession)
async def get_session(
    session_id: int,
    user: CurrentUserDep,
    session: AsyncSessionDep,
):
    return await chat_session_service.get_session(
        session=session, session_id=session_id, user=user
    )
