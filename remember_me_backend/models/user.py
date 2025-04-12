from sqlalchemy import Boolean, Column, String

from remember_me_backend.models.base import DBModel
from sqlalchemy.orm import relationship


class User(DBModel):
    __tablename__ = "users"

    # Mandatory
    email = Column(String, unique=True, index=True, nullable=False)

    # Defaulted
    is_active = Column(Boolean, default=True)

    # Nullable
    full_name = Column(String, nullable=True)

    # Relationships
    chat_sessions = relationship("ChatSession", back_populates="user")

