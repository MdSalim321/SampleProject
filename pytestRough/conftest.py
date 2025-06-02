import pytest

@pytest.fixture(scope="class")
def input_data():
    total = 100
    return total