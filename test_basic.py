# import pytest

def test_m1():
    a= 3
    b= 4
    assert a+1==b, "test failed"
   # assert a==b, "a is not equal to b"

def test_m2():
    name = "selim"
    assert  name.upper() == "SELIM"


def test_m3():
    True
def test_m4():
    False

def test_m5():
    assert "selim" == "selimn"

def test_m6():
    assert 100 == 101

def test_login():
    assert "admin" == "admin"