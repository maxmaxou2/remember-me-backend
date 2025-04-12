import pytest

from remember_me_backend.services.chat_session import (
    create_chat_session,
    get_chat_session,
)


class TestChatSessionService:
    @pytest.mark.asyncio
    async def test_create_chat_session(self, db_session, user):
        chat_session = await create_chat_session(db_session, user, title="oui")
        await db_session.refresh(user)
        assert chat_session.user_id == user.id

    @pytest.mark.asyncio
    async def test_get_chat_session(self, db_session, chat_session):
        await db_session.refresh(chat_session, ["user"])
        chat_session_received = await get_chat_session(
            db_session, chat_session.user, chat_session_id=chat_session.id
        )
        assert chat_session_received.id == chat_session.id
