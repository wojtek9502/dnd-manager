
from sqlalchemy import Column, UUID, String, Integer

from app.modules.common.BaseModel import BaseModel
from app.modules.common.mixins import InsertedOnMixin, UpdatedOnMixin

MODULE_PREFIX = 'us_'


class UserModel(BaseModel, InsertedOnMixin, UpdatedOnMixin):
    __tablename__ = MODULE_PREFIX + 'user'
    __uuid_column_name__ = 'id'

    id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(String(512), unique=True, nullable=False)
    password_hash = Column(String(512), nullable=False)
    salt = Column(String(256), nullable=False)
    hash_algo = Column(String(10), nullable=False)
    iterations = Column(Integer(), nullable=False)
