from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from remember_me_backend.core import settings

sync_engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed only for SQLite
)
sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

Base = declarative_base()
Base.metadata.create_all(bind=sync_engine)


class DBModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
