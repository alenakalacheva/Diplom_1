import pytest
from bun import Bun
from ingredient import Ingredient
from database import Database


@pytest.fixture
def bun():
    return Bun('Булочка', 50)


@pytest.fixture
def ingredient():
    return Ingredient('начинка', 'Сыр', 20)


@pytest.fixture
def database():
    database = Database()
    return database
