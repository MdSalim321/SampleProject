import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    print("I will execute first")
    driver.get("https://www.youtube.com/watch?v=9X3CKJNzqiU")
    driver.maximize_window()
    tlt = driver.title
    print("Title is: ", tlt)
    driver.save_screenshot("ScreenShotFolder/ScreenShot4.jpg")

# Here browser open & other prerequisite activity can be performed
    yield
    print("I will be executed last")
    driver.quit()

