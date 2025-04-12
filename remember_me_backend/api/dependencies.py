from typing import Annotated, TypeAlias

from fastapi import Depends, Request
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette import status as httpstatus

from remember_me_backend.models import User, sync_session_maker


async def get_db_session() -> Session:
    db = sync_session_maker()
    try:
        yield db
    finally:
        db.close()


# TODO: Remove the wizard logic and implement zitadel auth flow
async def get_current_user(
    request: Request, db_session: Session = Depends(get_db_session)
) -> User:
    # To be removed upon auth implementation
    state = getattr(request, "state", {})
    base_user = getattr(
        state,
        "user",
        type("BaseUser", (), {"email": "maxrossignol@hotmail.fr"})(),
    )
    user = db_session.query(User).filter(User.email == base_user.email).first()
    if not user:
        raise HTTPException(
            status_code=httpstatus.HTTP_401_UNAUTHORIZED, detail="Is not authenticated"
        )

    return user


CurrentUserDep: TypeAlias = Annotated[User, Depends(get_current_user)]
SyncSessionDep: TypeAlias = Annotated[Session, Depends(get_db_session)]
