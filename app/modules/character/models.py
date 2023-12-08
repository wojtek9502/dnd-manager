from sqlalchemy import *

from app.modules.common.Database import Database


class CharacterModel(Database):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)