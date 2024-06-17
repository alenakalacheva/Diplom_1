import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from data import TestIngredients


@pytest.fixture
def bun():
    return Bun(TestIngredients.SIMPLE_BUN, TestIngredients.SIMPLE_BUN_PRICE)


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, TestIngredients.CHEESE, TestIngredients.CHEESE_PRICE)


@pytest.fixture
def database():
    database = Database()
    return database
