from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.implicitly_wait(10)

# JS Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
time.sleep(4)
alert.accept()

# JS Confirm
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(4)
alert = driver.switch_to.alert
time.sleep(4)
alert.dismiss()  # or alert.accept()

# JS Prompt
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
alert.send_keys("Test input")
alert.accept()

time.sleep(2)
driver.quit()
