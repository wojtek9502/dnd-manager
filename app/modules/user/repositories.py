import hashlib
import os
import secrets
import uuid

from app.modules.common.BaseRepository import BaseRepository
from app.modules.user.models import UserModel


class UserRepository(BaseRepository):
    def model_class(self):
        return UserModel

    @staticmethod
    def _create_secure_password(password: str):
        pepper = os.environ['USER_AUTH_KEY']
        salt_token_bytes = int(os.environ['USER_AUTH_TOKEN_BYTES'])
        iterations = int(os.environ['USER_AUTH_HASH_N_ITERATIONS'])

        salt = secrets.token_bytes(salt_token_bytes)
        hash_value = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8') + pepper.encode('utf-8'),
            salt,
            iterations
        )
        password_hash = salt + hash_value
        return password_hash

    def create(self, username: str, password_clear: str) -> UserModel:
        password_hash = self._create_secure_password(password=password_clear)
        salt, hash_key = password_hash[:16], password_hash[16:]
        hash_algo = "PBKDF2"
        iterations = int(os.environ['USER_AUTH_HASH_N_ITERATIONS'])

        entity = UserModel(
            username=username,
            password_hash=hash_key,
            salt=salt,
            hash_algo=hash_algo,
            iterations=iterations
        )
        return entity

    def update(self, entity: UserModel, username: str, password_clear: str) -> UserModel:
        password_hash = self._create_secure_password(password=password_clear)
        salt, hash_key = password_hash[:16], password_hash[16:]
        hash_algo = "PBKDF2"
        iterations = int(os.environ['USER_AUTH_HASH_N_ITERATIONS'])

        entity.username = username
        entity.password_hash = hash_key
        entity.salt = salt
        entity.hash_algo = hash_algo
        entity.iterations = iterations

        self.commit()
        return entity

    def find_by_username(self, username: str):
        return self.query().filter(UserModel.username == username).one()

    def delete_by_username(self, username: str) -> uuid.UUID:
        query = self.query().filter(UserModel.username == username)
        entity = query.one()
        entity_id = entity.id

        query.delete()
        self.commit()
        return entity_id