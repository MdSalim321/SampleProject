from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
time.sleep(4)
driver.implicitly_wait(10)

driver.get("https://www.orangehrm.com/en/book-a-free-demo")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(By.XPATH, "(//select[contains(@class,'dropdown')])[1]"))


time.sleep(3)
country = driver.find_element(By.XPATH, "(//select[contains(@class,'dropdown')])[1]")
countryDropdown = Select(country)
countryDropdown.select_by_visible_text("India")






