class TestString:

    """Проверка команды concat()"""
    def test_string_one(self, fixture_four):
        assert fixture_four + " testing" == "test testing"

    """Проверка команды repeat()"""
    def test_string_two(self, fixture_four):
        assert (fixture_four * 5) == "testtesttesttesttest"

    """Проверка команды len()"""
    def test_string_three(self, fixture_four):
        assert len(fixture_four) == 4

    """Проверка команды get()"""
    def test_string_four(self, fixture_four):
        assert fixture_four[2] == 's'

    """Проверка команды isalpha()"""
    def test_string_five(self, fixture_four):
        assert fixture_four.isalpha()
        assert not fixture_four.isdigit()
