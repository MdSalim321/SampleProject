from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver =webdriver.Chrome()


driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.orangehrm.com/en/book-a-free-demo")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Your Full Name')]").send_keys("Abcd")
time.sleep(2)

wait=WebDriverWait (driver, 20)

PhNumber = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Phone Number')]")))
PhNumber.send_keys("9876543210")
time.sleep(3)

email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Business Email')]")))
email.send_keys("john@example.com")

companyName = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Company Name')]")))
companyName.send_keys("abc Pvt ltd")

time.sleep(3)
country = driver.find_element(By.XPATH, "(//select[contains(@class,'dropdown')])[1]")
countryDropdown = Select(country)
countryDropdown.select_by_visible_text("India")

time.sleep(3)
employeeNumber = driver.find_element(By.XPATH, "(//select[contains(@class,'dropdown')])[2]")
employeeNumberDropdown = Select(employeeNumber)
employeeNumberDropdown.select_by_visible_text("200 - 1,000")

driver.switch_to.frame()












