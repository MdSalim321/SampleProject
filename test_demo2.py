# Any pytest file should start with test_
# Method name should start with test_
# Any Code should be wrapped in a method only
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Both message does not matches"

@pytest.mark.xfail
def test_secondCreditCard():
    a =4
    b= 6
    assert a+2 == 6, "Assertion does not match"

@pytest.fixture()
def setup():
    print("I will execute first")
# Here browser open & other prerequisite activity can be performed


def fixtureDemo(setup):
    print("I will execute steps in the fixture Demo")


def test_login():
    assert "admin" == "admin"







