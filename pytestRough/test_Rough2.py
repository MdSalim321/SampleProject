import pytest

@pytest.mark.usefixtures("input_data")
class Test_Divisibilityy:
    def test_divisible_3(self, input_data):
        assert input_data % 6 == 0, "Not divisible by 6"


    def test_divisible_4(self, input_data):
        assert input_data % 7 == 0, "Not divisible by 7"