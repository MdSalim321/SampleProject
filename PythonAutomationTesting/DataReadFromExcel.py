import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from openpyxl import load_workbook

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
workbook = load_workbook("DataSet/DataSheet.xlsx")
sheet = workbook ["Sheet1"]

uName = sheet["A2"].value
passW = sheet["B2"].value

time.sleep(5)
print(uName)
print(passW)

Wait = WebDriverWait(driver, 20)
Username = Wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
Username.send_keys(uName)

Password = Wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
Password.send_keys(passW)

Submit_button = Wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Login']")))
Submit_button.click()