import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient


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
