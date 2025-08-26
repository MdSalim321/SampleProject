import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo/fontawesome-icons.html")

rightClickButton = driver.find_element(By.XPATH, "//span[text()='right click me']")
wait = WebDriverWait(driver, 10)

ac = ActionChains(driver)
time.sleep(3)
ac.context_click(rightClickButton).perform()

menu_items = driver.find_elements(By.CSS_SELECTOR, "ul.context-menu-list li.context-menu-item")
total_items = len(menu_items)
print("Total Menu Items Found:", total_items)






