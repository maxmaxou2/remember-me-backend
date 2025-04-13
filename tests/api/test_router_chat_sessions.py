import pytest
import time_machine
from inline_snapshot import snapshot
import pandas as pd


class TestRouterChatSessions:
    ROUTER_PREFIX = "api/v1/chatsessions"

    @pytest.mark.asyncio
    @time_machine.travel(pd.Timestamp("2025-01-01", tz="CET"), tick=False)
    async def test_create_chat_session(self, client):
        response = await client.post(f"{self.ROUTER_PREFIX}/create")

        assert response.status_code == 200
        assert "id" in response.json()
        assert "created_at" in response.json()
        assert "updated_at" in response.json()
        assert response.json() == snapshot(
            {
                "title": None,
                "description": None,
                "updated_at": "2024-12-31T23:00:00",
                "created_at": "2024-12-31T23:00:00",
                "id": 1,
                "transcript": None,
                "summary": None,
            }
        )

    @pytest.mark.asyncio
    async def test_get_chat_session(self, client, chat_session, db_session):
        await db_session.refresh(chat_session)
        response = await client.get(f"{self.ROUTER_PREFIX}/{chat_session.id}")

        assert response.status_code == 200
        assert "id" in response.json()
        assert "created_at" in response.json()
        assert "updated_at" in response.json()
        assert response.json() == snapshot(
            {
                "title": None,
                "description": None,
                "updated_at": "2024-12-31T23:00:00",
                "created_at": "2024-12-31T23:00:00",
                "id": 1,
                "transcript": None,
                "summary": None,
            }
        )
