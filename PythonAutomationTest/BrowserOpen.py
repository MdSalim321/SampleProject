import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH , "//input[@placeholder='Password']")
password.send_keys("admin123")

submitButton = driver.find_element(By.XPATH ,"//button[normalize-space()='Login']")
submitButton.click()
time.sleep(2000)
print("Successfully Login")
time.sleep(2000)

admin = driver.find_element(By.XPATH, "//a[contains(@class, 'oxd-main-menu-item active')]/span")
admin.click()
time.sleep(2000)

userNameField = driver.find_element(By.XPATH, "(//input[contains(@class,'oxd-input oxd-input--active')])[2]")
userNameField.send_keys("Test")
time.sleep(2000)

UserRole = driver.find_element(By.XPATH, "(//div[contains(@class, 'oxd-select-text oxd-select-text--active')])[1]")
s = Select(UserRole)
s.select_by_visible_text("Admin")
time.sleep(2000)

empName = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
empName.send_keys("Testing")
time.sleep(2000)

status = driver.find_element(By.XPATH, "(//div[contains(@class, 'oxd-select-text oxd-select-text--active')])[2]")
s1 = Select(status)
s1.select_by_visible_text("Enabled")
time.sleep(2000)

submitButton = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
submitButton.click()
time.sleep(2000)









