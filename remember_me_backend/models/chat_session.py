from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from remember_me_backend.models.base import DBModel


class ChatSession(DBModel):
    __tablename__ = "chat_sessions"

    # Mandatory
    title = Column(String, nullable=False)
    transcript = Column(Text, nullable=False)

    # Nullable
    description = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)

    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="sessions")
