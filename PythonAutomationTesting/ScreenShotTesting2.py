from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()

os.makedirs("ScreenShotFolder4", exist_ok= True )

ttl_act = driver.title
ttl_expect = "Soogle"
time.sleep(4)

try:
    assert ttl_act == ttl_expect, "Title does not match"

except AssertionError as f:

    driver.save_screenshot("ScreenShotFolder4/screenshot2.jpg")
finally:
    driver.quit()
