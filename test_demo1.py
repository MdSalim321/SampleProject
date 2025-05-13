# Any pytest file should start with test_
# Method name should start with test_
# Any Code should be wrapped in a method only
import pytest


@pytest.mark.smoke
def test_firstProgramse(setup):
    print("Hello ")


def test_secondGreetings():
    print("Good mornimg ")

def test_login():
    assert "admin" == "admin"




