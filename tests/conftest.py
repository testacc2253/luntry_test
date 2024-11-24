import pytest
from clients import BaseClient


@pytest.fixture(scope="session")
def base_client():
    return BaseClient()
