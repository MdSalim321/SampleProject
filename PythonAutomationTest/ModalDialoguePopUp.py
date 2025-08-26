import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(@id, 'showSmallModal')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(@id, 'closeSmallModal')]").click()
time.sleep(5)




