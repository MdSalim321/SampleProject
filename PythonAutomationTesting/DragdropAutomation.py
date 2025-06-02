
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

# Switch to iframe if required (jqueryui uses iframes)
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Identify source and target elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

time.sleep(3)

