from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

Wait=WebDriverWait (driver, 20)

Username = Wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
Username.send_keys("Admin")

Password = Wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
Password.send_keys("admin123")

Submit_button = Wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Login']")))
Submit_button.click()





time.sleep(5)
















