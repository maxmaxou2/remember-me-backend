from remember_me_backend.models import ChatSession, User


async def create_session(
    session: ChatSession, title: str, description: str, content: str, user: User
) -> ChatSession:
    chat_session = ChatSession(
        title=title, description=description, content=content, user=user
    )

    session.add(chat_session)
    session.commit()

    return chat_session


def get_session(session: ChatSession, session_uuid: int):
    return session.query(ChatSession).filter(ChatSession.uuid == session_uuid).first()
