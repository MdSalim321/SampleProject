import pytest
from selenium import webdriver

@pytest.mark.usefixtures("init_driver")
class Test_Google():

    def test_Google_Title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

    def test_Google_Url(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.current_url == "https://www.google.com/"


