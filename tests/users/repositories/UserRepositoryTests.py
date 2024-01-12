from app.modules.user.repositories import UserRepository
from tests.utils.BaseTest import BaseTest


class UserRepositoryTests(BaseTest):
    def test_create_user(self):
        # given
        username = 'test'
        password_clear = 'pass'
        repo = UserRepository()

        # when
        entity = repo.create(
            username=username,
            password_clear=password_clear
        )
        repo.save(entity)
        repo.commit()

        # then
        assert entity.username == username
        assert entity.password_hash != password_clear
        assert entity.hash_algo
        assert entity.salt
        assert entity.iterations

    def test_find_by_username(self):
        # given
        username = 'test'
        password_clear = 'pass'
        repo = UserRepository()
        origin_entity = repo.create(
            username=username,
            password_clear=password_clear
        )
        origin_entity_id = origin_entity.id
        repo.save(origin_entity)
        repo.commit()

        # when
        found_entity = repo.find_by_username(username=username)

        # then
        assert origin_entity_id == found_entity.id

    def test_update_user(self):
        # given
        username = 'test'
        origin_password = 'pass'
        new_password = 'new_pass'

        repo = UserRepository()
        origin_entity = repo.create(
            username=username,
            password_clear=origin_password
        )
        origin_password_hash = origin_entity.password_hash
        repo.save(origin_entity)
        repo.commit()

        # when
        updated_entity = repo.update(
            entity=origin_entity,
            username=username,
            password_clear=new_password
        )

        # then
        assert updated_entity.username == username
        assert origin_entity.password_hash != origin_password_hash

    def test_delete_user(self):
        # given
        username = 'test'
        password_clear = 'pass'
        repo = UserRepository()

        entity = repo.create(
            username=username,
            password_clear=password_clear
        )
        entity_id = entity.id
        repo.save(entity)
        repo.commit()

        # when
        deleted_entity_id = repo.delete_by_username(username=username)

        # then
        assert not len(repo.find_all())
        assert deleted_entity_id == entity_id