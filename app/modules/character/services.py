from app import CharacterModel
from app.modules.character.repositories import CharacterRepository


class CharacterService:
    def add_character(self) -> CharacterModel:
        repo = CharacterRepository()
        entity = repo.create()
        repo.save(entity)
        repo.commit()

        return entity