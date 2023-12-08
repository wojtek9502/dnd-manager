from app.modules.character.repositories import CharacterRepository


class CharacterService:
    def add_character(self, _id: int):
        repo = CharacterRepository()
        entity = repo.create(
            _id=_id
        )
        repo.save(entity)
        repo.commit()