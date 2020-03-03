import random
import pytest


@pytest.fixture(scope="function")
def random_number():
    return random.randint(6, 10)


@pytest.fixture(scope="function")
def fixture_one():
    return [1, 2, 3, 4, 5, 6]


@pytest.fixture(scope="function")
def fixture_two(request):
    return {1, 2, 3, 4, 5}


@pytest.fixture(scope="function")
def fixture_three():
    return {
        "Number": "One",
        "Color": "Black",
        "Size": 15
    }


@pytest.fixture(scope="function")
def fixture_four():
    return "test"


class TestCase:
    def __init__(self, case1, case2):
        self.case1 = case1
        self.case2 = case2

    def return_color(self):
        return "Red"


@pytest.fixture(scope="function")
def fixture_return_class():
    return TestCase(case1=1, case2=2)
