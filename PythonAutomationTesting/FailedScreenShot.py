from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Google
    driver.get("https://www.google.com")
    time.sleep(2)  # Wait for page to load

    # Check title
    expected_title = "Google"
    actual_title = driver.title
    print("Page:", actual_title)

    assert actual_title == expected_title, "Title does not match!"

except AssertionError as e:
    driver.save_screenshot("ScreenShotFolder/ScreenShot7.png")

finally:
    # Close browser
    driver.quit()
