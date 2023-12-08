from app.modules.character.repositories import CharacterRepository
from app.modules.character.services import CharacterService
from tests.utils.BaseTest import BaseTest


class CharacterServiceTest(BaseTest):
    def test_a(self):
        # given
        service = CharacterService()

        # when
        service.add_character(_id=2)
        entity = CharacterRepository().get_by_id(2)

        # then
        assert entity
