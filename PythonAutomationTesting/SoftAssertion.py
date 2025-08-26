import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
wait = WebDriverWait(driver, 10)
userName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Username']")))
#userName = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
userName.send_keys("Admin")
time.sleep(3)
passWord = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']")))
#passWord = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
passWord.send_keys("admin123")
time.sleep(3)
submitButton = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
submitButton.click()
time.sleep(5)







