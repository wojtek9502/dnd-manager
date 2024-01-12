from sqlalchemy import *

from app.modules.common.BaseModel import BaseModel
from app.modules.common.mixins import InsertedOnMixin, UpdatedOnMixin

MODULE_PREFIX = 'cr_'


class CharacterModel(BaseModel, InsertedOnMixin, UpdatedOnMixin):
    __tablename__ = MODULE_PREFIX + 'character'
    __uuid_column_name__ = 'id'

    id = Column(UUID(as_uuid=True), primary_key=True)