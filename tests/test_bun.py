from data import TestIngredients
class TestBun:

    def test_bun_name(self, bun):
        assert bun.get_name() == TestIngredients.SIMPLE_BUN

    def test_bun_price(self, bun):
        assert bun.get_price() == TestIngredients.SIMPLE_BUN_PRICE
