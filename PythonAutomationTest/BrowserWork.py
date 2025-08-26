from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
time.sleep(3)
search_box.send_keys("Selenium Python")
time.sleep(3)
search_box.submit()
time.sleep(3)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
time.sleep(3)
driver.quit()

