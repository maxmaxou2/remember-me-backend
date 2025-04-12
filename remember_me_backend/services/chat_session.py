import sqlalchemy as sa

from remember_me_backend.models import AsyncSession, ChatSession, User


async def create_chat_session(
    session: AsyncSession,
    user: User,
    title: str | None = None,
    description: str | None = None,
) -> ChatSession:
    chat_session = ChatSession(title=title, description=description, user=user)

    session.add(chat_session)
    await session.commit()
    await session.refresh(chat_session)

    return chat_session


async def get_chat_session(
    session: AsyncSession, user: User, chat_session_id: int
) -> ChatSession:
    query = sa.select(ChatSession).filter(
        ChatSession.id == chat_session_id, ChatSession.user == user
    )
    result = await session.execute(query)
    return result.scalars().one()
