from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

with open("DataSet/Data.txt", "r") as f:
    lines = f.readlines()

userName = lines[0].strip()
passWord = lines[1].strip()

print(userName)
print(passWord)

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)

userNameXpath = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
time.sleep(3)
userNameXpath.send_keys(userName)

passWordXpath = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
time.sleep(3)
passWordXpath.send_keys(passWord)

loginButton = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Login']")))
time.sleep(3)
loginButton.click()

time.sleep(5)
