class TestDatabase:
    def test_count_buns(self, database):
        assert len(database.buns) == 3


    def test_count_ingredients(self, database):
        assert len(database.ingredients) == 6