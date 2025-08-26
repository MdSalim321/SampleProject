import time
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()
driver.implicitly_wait(5)

addButton = driver.find_element(By.XPATH, "//button[normalize-space()='Add Element']")
time.sleep(3)
driver.execute_script("arguments[0].click();", addButton)
time.sleep(3)

delButton = driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")
driver.execute_script("arguments[0].click();", delButton)

# Get actual and expected titles
act_Title = driver.title
ex_Title = "The Interne"

if ex_Title != act_Title:
    print(f"Expected title: {ex_Title} & does not match with actual title: {act_Title}")

    # Create folder if not exists
    os.makedirs("ScreenShotPath", exist_ok=True)

    # Generate timestamp for unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scPath = f"ScreenShotPath/sc_{timestamp}.png"

    # Save the screenshot
    driver.save_screenshot(scPath)
    print(f"Screenshot saved at: {scPath}")

else:
    print("Title perfectly matched")

time.sleep(3)
driver.quit()
