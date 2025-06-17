import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create screenshot folder if it doesn't exist
screenshot_folder = "ScreenShotFolder"
os.makedirs(screenshot_folder, exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(3)
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Alert')]").click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(3)

    ttl = driver.title
    print(ttl)

    # Assertion
    assert ttl == "The Inter", "Page title mismatch!"  # This will fail intentionally

except AssertionError as ee:
    print("Assertion Error:", str(ee))
    # Take screenshot if assertion fails
    screenshot_path = os.path.join("/ScreenShotFolder", "assertionFailed.jpg")
    driver.save_screenshot(screenshot_path)

finally:
    driver.quit()
