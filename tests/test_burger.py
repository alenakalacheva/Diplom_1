from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булочка"
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_set_ingredient(self):
        burger = Burger()
        mock_cheese = Mock()
        mock_souse = Mock()
        burger.add_ingredient(mock_cheese)
        burger.add_ingredient(mock_souse)
        assert burger.ingredients == [mock_cheese, mock_souse]

    def test_remove_ingredient(self):
        burger = Burger()
        mock_cheese = Mock()
        burger.add_ingredient(mock_cheese)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_cheese = Mock()
        mock_souse = Mock()
        burger.add_ingredient(mock_cheese)
        burger.add_ingredient(mock_souse)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_souse, mock_cheese]

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50
        mock_cheese = Mock()
        mock_cheese.get_price.return_value = 100
        burger.bun = mock_bun
        burger.ingredients = [mock_cheese]
        assert burger.get_price() == 200

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50
        mock_bun.get_name.return_value = 'Ржаная булка'
        mock_cheese = Mock()
        mock_cheese.get_price.return_value = 100
        mock_cheese.get_name.return_value = 'Сыр'
        mock_cheese.get_type.return_value = 'начинка'
        burger.bun = mock_bun
        burger.ingredients = [mock_cheese]
        assert burger.get_receipt() == '(==== Ржаная булка ====)\n= начинка Сыр =\n(==== Ржаная булка ====)\n\nPrice: 200'










