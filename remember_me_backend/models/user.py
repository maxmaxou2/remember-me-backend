from sqlalchemy import Boolean, Column, String

from remember_me_backend.models.base import DBModel


class User(DBModel):
    __tablename__ = "users"

    # Mandatory
    email = Column(String, unique=True, index=True, nullable=False)

    # Defaulted
    is_active = Column(Boolean, default=True)

    # Nullable
    full_name = Column(String, nullable=True)
