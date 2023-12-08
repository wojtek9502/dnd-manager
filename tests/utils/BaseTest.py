from unittest import TestCase

from sqlalchemy import inspect, text
from sqlalchemy.orm import sessionmaker

from app import engine


class BaseTest(TestCase):
    def setUp(self):
        self.before_test_start()

    def tearDown(self):
        ...

    def before_test_start(self):
        self.cleanup_db()

    @staticmethod
    def cleanup_db():
        db_inspect = inspect(engine)
        tables = sorted(db_inspect.get_table_names())

        connection = engine.connect()
        transaction = connection.begin()
        try:
            for table in reversed(tables):
                sql = text(f"TRUNCATE TABLE {table} CASCADE")
                connection.execute(statement=sql)
            transaction.commit()
        except Exception:
            transaction.rollback()
            raise
