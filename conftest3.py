import pytest

@pytest.fixture(scope= "class")
def dataLoad():
    print("User profile data, pass from the this conftest")
    return ["Selim", "Shaikh", "My name is Selim"]

@pytest.fixture(params= [("chrome","Selim", "Bhai"), ("Firefox","Test", "Anything"), ("IE", "SS","SP")])
def crossBrowser(request):
    return request.param


  
