import pytest



@pytest.mark.parametrize("num,result", [(1,11), (2, 22), (3,33), (5,55)])
def test_calculation(num, result):
    assert num*11 == result



