import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import none_of
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def tearDown_module():
    driver.quit()

def test_googleTitle():
    assert driver.title == "Google"

def test_googleUrl():
    assert driver.current_url == "https://www.google.com/"




