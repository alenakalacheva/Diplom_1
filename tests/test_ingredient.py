class TestIngredient:
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 20

    # Тест для проверки названия ингредиента
    def test_get_name(self, ingredient):
        assert ingredient.get_name() == 'Сыр'

    # Тест для проверки типа ингредиента
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == 'начинка'

