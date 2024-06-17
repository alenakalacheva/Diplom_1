class TestDatabase:
    def test_count_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_count_ingredients(self, database):
        assert len(database.available_ingredients()) == 6
