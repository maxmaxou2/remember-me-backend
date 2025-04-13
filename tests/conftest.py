import os
from typing import Iterator

import httpx
import pandas as pd
import pytest_asyncio
import time_machine
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from remember_me_backend.api import dependencies
from remember_me_backend.app import make_app
from remember_me_backend.models import ChatSession, DBModel, User
from tests.factory import mixer

UNITTEST_DATABASE_URL = os.getenv(
    "UNITTEST_DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/remember_me_backend_unittest",
)
ROUTER_PREFIX = os.getenv("ROUTER_PREFIX", "/api/v1")


@pytest_asyncio.fixture(scope="function")
def app() -> FastAPI:
    return make_app()


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
    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture
async def client(app, db_session, user):
    app.dependency_overrides[dependencies.get_db_session] = lambda: db_session
    app.dependency_overrides[dependencies.get_current_user] = lambda: user

    transport = httpx.ASGITransport(
        app=app,
        raise_app_exceptions=True,
    )
    async with httpx.AsyncClient(
        transport=transport, base_url="http://localhost"
    ) as client:
        yield client

    for dep in (dependencies.get_db_session, dependencies.get_current_user):
        app.dependency_overrides.pop(dep)


@pytest_asyncio.fixture
async def user(db_session):
    user = mixer.blend(User)
    db_session.add(user)
    await db_session.commit()
    return user


@pytest_asyncio.fixture
@time_machine.travel(pd.Timestamp("2025-01-01", tz="CET"), tick=False)
async def chat_session(user, db_session):
    chat_session = mixer.blend(ChatSession, user=user)
    db_session.add(chat_session)
    await db_session.commit()
    return chat_session
