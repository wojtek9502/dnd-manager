from app.modules.character.repositories import CharacterRepository
from app.modules.character.services import CharacterService
from tests.utils.BaseTest import BaseTest


class CharacterServiceTest(BaseTest):
    def test_create_character(self):
        # given
        service = CharacterService()
        entity = service.add_character()
        entity_id = entity.id

        # when
        entity = CharacterRepository().get_by_id(entity_id)

        # then
        assert entity
