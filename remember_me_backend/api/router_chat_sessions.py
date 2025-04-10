from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from remember_me_backend.api.dependencies import CurrentUserDep, SyncSessionDep
from remember_me_backend.services import session_service


class ChatSessionBase(BaseModel):
    title: str
    description: str | None = None


class ChatSessionCreate(ChatSessionBase):
    pass


class ChatSession(ChatSessionBase):
    id: int
    audio_file_path: str | None = None
    transcript: str | None = None
    summary: str | None = None
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


router = APIRouter()


@router.post("/", response_model=ChatSession)
async def create_session(
    title: str,
    content: str,
    user: CurrentUserDep,
    session: SyncSessionDep,
    description: str | None = None,
):
    return await session_service.create_session(
        session=session,
        title=title,
        content=content,
        description=description,
        user=user,
    )


@router.get("/{session_uuid}", response_model=ChatSession)
def get_session(
    session_uuid: int,
    user: CurrentUserDep,
    session: SyncSessionDep,
):
    return session_service.get_session(
        session=session, session_uuid=session_uuid, user=user
    )
