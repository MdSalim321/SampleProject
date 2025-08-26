import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
driver.implicitly_wait(5)

dropdown_element = driver.find_element(By.XPATH, "//select[contains(@id, 'dropdown')]")
s = Select(dropdown_element)
time.sleep(2)
s.select_by_value("1")
time.sleep(2)
driver.quit()




