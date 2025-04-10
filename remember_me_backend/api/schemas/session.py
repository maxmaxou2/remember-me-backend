from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SessionBase(BaseModel):
    title: str
    description: Optional[str] = None


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id: int
    audio_file_path: Optional[str]
    transcript: Optional[str]
    summary: Optional[str]
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
