from __future__ import annotations

import asyncio
from pprint import pprint

import sqlalchemy as sa
import typer

try:
    pprint = __import__("devtools").debug
except ImportError:
    pass


app = typer.Typer()


@app.command("init-db")
def init_db() -> None:
    from remember_me_backend.models.base import init_db
    asyncio.run(init_db())


@app.command("seed-db")
def seed_db() -> None:
    from remember_me_backend.models import User, async_session_maker

    email = "maxrossignol@hotmail.fr"
    async def _wrapper():
        async with async_session_maker() as session:
            query = sa.select(User).filter(User.email == email)
            result = await session.execute(query)
            existing_user = result.scalars().first()

            if not existing_user:
                user = User(email=email)
                session.add(user)
                await session.commit()
                print(f"Created user with email: {email}")
            else:
                print(f"User with email {email} already exists")

    asyncio.run(_wrapper())


if __name__ == "__main__":
    app()
