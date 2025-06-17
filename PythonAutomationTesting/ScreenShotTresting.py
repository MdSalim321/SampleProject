from selenium import webdriver
import os

# Ensure folder exists
os.makedirs("ScreenShotFolder3", exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
exp_ttl = "Google";
act_ttl = driver.title
print(act_ttl)



try:
    assert act_ttl == exp_ttl, "Title mismatch"

except AssertionError as e:
    driver.save_screenshot("ScreenShotFolder3/ScreenShot1.jpg")

driver.quit()
