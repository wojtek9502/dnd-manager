from typing import Any

from app.modules.character.models import CharacterModel
from app.modules.common.BaseRepository import BaseRepository


class CharacterRepository(BaseRepository):
    def model_class(self):
        return CharacterModel

    def create(self):
        entity = CharacterModel()
        return entity
