from data import TestIngredients
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
class TestIngredient:
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == TestIngredients.CHEESE_PRICE

    # Тест для проверки названия ингредиента
    def test_get_name(self, ingredient):
        assert ingredient.get_name() == TestIngredients.CHEESE

    # Тест для проверки типа ингредиента
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

