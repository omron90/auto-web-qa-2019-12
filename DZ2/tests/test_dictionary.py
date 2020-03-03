class TestDictionary:

    """Проверка команды clear()"""

    def test_dictionary_one(self, fixture_three, random_number):
        dict1 = fixture_three
        dict1.clear()
        assert len(dict1) == 0

    """Проверка команды pop()"""

    def test_dictionary_two(self, fixture_three):
        dictionary = fixture_three
        count_values = 0
        assert dictionary.pop("Size") == 15
        for x in dictionary.values():
            count_values += 1
        assert count_values == 2

    """Проверка команды get()"""

    def test_dictionary_three(self, fixture_three):
        assert fixture_three.get("Size") == 15

    """Проверка команды update()"""

    def test_dictionary_four(self, fixture_three):
        fixture_three.update({"Size": 15, "Ex": "null"})
        assert fixture_three == {
            "Number": "One",
            "Color": "Black",
            "Size": 15,
            "Ex": "null"
        }

    """Проверка команды setdefault()"""

    def test_dictionary_five(self, fixture_three):
        assert fixture_three.setdefault("Ex", "null") == fixture_three.get("Ex")
