from uuid import uuid4

from faker import Faker

from src.auth.domain.entity import AuthCredential
from src.shared.application.mappers import dict_to_entity
fake = Faker()


class AuthCredentialFactory:

    @classmethod
    def build(cls, **kwargs) -> AuthCredential:
        return dict_to_entity(AuthCredential, cls.to_dict(**kwargs))

    @staticmethod
    def to_dict( 
            user_id: str = uuid4(),
            username: str = fake.email(),
            password: str = fake.password()
        ) -> dict:
        return {
            'user_id': user_id,
            'username': username,
            'password': password
        }
