from remember_me_backend.models import ChatSession, User


async def create_session(
    session: ChatSession, title: str, description: str, content: str, user: User
) -> ChatSession:
    chat_session = ChatSession(
        title=title, description=description, transcript=content, user=user
    )

    session.add(chat_session)
    session.commit()

    return chat_session


async def get_session(session: ChatSession, session_id: int, user: User):
    return (
        session.query(ChatSession)
        .filter(ChatSession.id == session_id, ChatSession.user == user)
        .first()
    )
