import abc
from typing import Any

from sqlalchemy.orm import sessionmaker

from app import engine


class BaseRepository(abc.ABC):
    Session = sessionmaker(bind=engine)
    session = Session()

    @abc.abstractmethod
    def model_class(self):
        ...

    def get_by_id(self, id_: Any):
        return self.session.get(self.model_class(), id_)

    def commit(self):
        self.session.commit()

    def save(self, entity):
        self.session.add(entity)
