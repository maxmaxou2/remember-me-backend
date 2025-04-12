from typing import Annotated, AsyncGenerator, TypeAlias

import sqlalchemy as sa
from fastapi import Depends, Request
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status as httpstatus

from remember_me_backend.models import User, async_session_maker


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db = async_session_maker()
    try:
        yield db
    finally:
        await db.close()


# TODO: Remove the wizard logic and implement zitadel auth flow
async def get_current_user(
    request: Request, db_session: AsyncSession = Depends(get_db_session)
) -> User:
    # To be removed upon auth implementation
    state = getattr(request, "state", {})
    base_user = getattr(
        state,
        "user",
        type("BaseUser", (), {"email": "maxrossignol@hotmail.fr"})(),
    )
    user_query = sa.select(User).filter(User.email == base_user.email)
    result = await db_session.execute(user_query)
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=httpstatus.HTTP_401_UNAUTHORIZED, detail="Is not authenticated"
        )

    return user


CurrentUserDep: TypeAlias = Annotated[User, Depends(get_current_user)]
AsyncSessionDep: TypeAlias = Annotated[AsyncSession, Depends(get_db_session)]
