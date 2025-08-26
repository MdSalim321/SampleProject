import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.implicitly_wait(10)

#Handling the Alert Popup1
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)

#Handling the 2nd Popup
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(3)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
time.sleep(3)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
txtAlert = driver.switch_to.alert
txtAlert.send_keys("Testing")
time.sleep(3)
txtAlert.accept()
time.sleep(3)

