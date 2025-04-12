import pytest
from tests.mixer_setup import mixer
from remember_me_backend.models import User, ChatSession

@pytest.fixture
def db_session():
    pass

@pytest.fixture
def user():
    return mixer.blend(User)

@pytest.fixture
def chat_session(user):
    return mixer.blend(ChatSession, user=user)
