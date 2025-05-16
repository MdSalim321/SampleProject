import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "ie"], scope="class")
def init_driver(request):
    if request.param == "chrome":
           web_driver =  webdriver.Chrome()
    elif request.param == "firefox":
           web_driver=  webdriver.Firefox()
    elif request.param == "ie":
           web_driver= webdriver.Ie()

    yield
    web_driver.quit()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_Google_Title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

    def test_Google_Url(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.current_url == "https://www.google.com/"