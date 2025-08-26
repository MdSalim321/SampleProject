import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# 1st Alert
jsPopUp = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
jsPopUp.click()

time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

# the 2nd alert
jsPopUps = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
jsPopUps.click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(3)

jsPopUpTxt = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]")
jsPopUpTxt.click()
time.sleep(5)
driver.switch_to.alert.send_keys("Testing")
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)




