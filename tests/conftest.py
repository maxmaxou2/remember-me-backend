import os
from typing import Iterator

import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from remember_me_backend.models import ChatSession, DBModel, User
from tests.factory import mixer

UNITTEST_DATABASE_URL = os.getenv(
    "UNITTEST_DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/remember_me_backend_unittest",
)


@pytest_asyncio.fixture(scope="function")
async def engine() -> Iterator[AsyncEngine]:
    engine = create_async_engine(UNITTEST_DATABASE_URL)

    async with engine.begin() as conn:
        await conn.run_sync(DBModel.metadata.drop_all)
        await conn.run_sync(DBModel.metadata.create_all)

    yield engine


@pytest_asyncio.fixture(scope="function")
async def db_session(engine: AsyncEngine) -> AsyncSession:
    async_session_maker = async_sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )

    # async with (
    #     engine.connect() as connection,
    #     connection.begin() as transaction,
    # ):
    #     session = AsyncSession(bind=connection, expire_on_commit=False)

    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture
async def user(db_session):
    user = mixer.blend(User)
    db_session.add(user)
    await db_session.commit()
    return user


@pytest_asyncio.fixture
async def chat_session(user, db_session):
    chat_session = mixer.blend(ChatSession, user=user)
    db_session.add(chat_session)
    await db_session.commit()
    return chat_session
