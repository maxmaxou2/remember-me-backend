from remember_me_backend.models import AsyncSession, ChatSession, User
import sqlalchemy as sa


async def create_session(
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


async def get_session(
    session: AsyncSession, session_id: int, user: User
) -> ChatSession:
    query = sa.select(ChatSession).filter(
        ChatSession.id == session_id, ChatSession.user == user
    )
    result = await session.execute(query)
    return result.scalars().one()
