from __future__ import annotations

from pprint import pprint

import sqlalchemy as sa
import typer

try:
    pprint = __import__("devtools").debug
except ImportError:
    pass


app = typer.Typer()


@app.command("seed-db")
def seed_db() -> None:
    from remember_me_backend.models import User, sync_session_maker

    session = sync_session_maker()

    email = "admin@example.com"
    existing_user = session.query(User).filter(User.email == email).first()

    if not existing_user:
        user = User(email=email)
        session.add(user)
        session.commit()
        print(f"Created user with email: {email}")
    else:
        print(f"User with email {email} already exists")
