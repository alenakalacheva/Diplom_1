class TestBun:

    def test_bun_name(self, bun):
        assert bun.get_name() == 'Булочка'

    def test_bun_price(self, bun):
        assert bun.get_price() == 50
