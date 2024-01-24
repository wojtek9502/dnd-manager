from fastapi.testclient import TestClient

from app import app
from tests.utils.BaseTest import BaseTest


class ApiBaseTest(BaseTest):
    test_api = TestClient(app)

