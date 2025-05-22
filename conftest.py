import pytest
from selenium import webdriver
import logging

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):

    if request.param == "chrome":
           web_driver =  webdriver.Chrome()
           web_driver.maximize_window()
    elif request.param == "firefox":
           web_driver=  webdriver.Firefox()
           web_driver.maximize_window()

    else:
        raise ValueError("Unsupported browser")
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()