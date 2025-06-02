from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager.install())
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()

@pytest.fixture(scope="class")
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()

@pytest.mark.usefixtures("init_chrome_driver")
class test_Base_chrome:
    pass

class test_google_chrome(test_Base_chrome):
    def test_google_chorome_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"


@pytest.mark.usefixtures("init_ff_driver")
class test_Base_firefox:
    pass

class test_google_firefox(test_Base_firefox):
    def test_google_firefox_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"