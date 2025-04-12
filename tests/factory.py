from typing import Any

import sqlalchemy as sa

# Assuming you have a faker instance from mixer
from faker import Faker
from mixer import mix_types as t
from mixer.backend.sqlalchemy import SKIP_VALUE
from mixer.backend.sqlalchemy import GenFactory as BaseGenFactory
from mixer.backend.sqlalchemy import Mixer as BaseMixer
from mixer.backend.sqlalchemy import TypeMixer as BaseTypeMixer
from remember_me_backend.models import ChatSession, User

faker = Faker()


class GenFactory(BaseGenFactory):  # Extend if needed
    types = BaseGenFactory.types | {
        sa.String: t.STRING,
        sa.Text: t.TEXT,
        sa.Boolean: t.BOOL,
        sa.Integer: t.INT,
    }


class TypeMixer(BaseTypeMixer):
    def get_value(self, field_name: str, field_value: Any) -> Any:
        field = self.__fields.get(field_name)
        if field and isinstance(field.scheme, sa.orm.RelationshipProperty):
            if field_value is SKIP_VALUE:
                return field_name, SKIP_VALUE
            else:
                return field_name, t._Deffered(field_value, field.scheme)
        return super().get_value(field_name, field_value)


class Mixer(BaseMixer):
    type_mixer_cls = TypeMixer


mixer = Mixer(factory=GenFactory, commit=False, session=None)

mixer.register(
    User,
    email=lambda: faker.email(),
    is_active=lambda: True,
    full_name=lambda: faker.name(),
)

mixer.register(
    ChatSession,
    title=lambda: faker.sentence(nb_words=4),
    transcript=lambda: faker.paragraph(nb_sentences=5),
    description=lambda: faker.paragraph(nb_sentences=3),
    summary=lambda: faker.sentence(),
    user=lambda: mixer.blend(User),
)
