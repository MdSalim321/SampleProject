import pytest


@pytest.mark.usefixtures("input_data")
class Test_Divisibility:

    def test_divisible_1(self, input_data):
        assert input_data % 10 == 0, "Not divisible by 10"


    def test_divisible_2(self, input_data):
        assert input_data % 3 == 0, "Not divisible by 3"