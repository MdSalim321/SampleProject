import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(3)
buttonRtClik = driver.find_element(By.XPATH, "//span[contains(text(), 'right click me')]")
ac = ActionChains(driver)
ac.context_click(buttonRtClik).perform()
time.sleep(3)

edit_option = driver.find_element(By.XPATH, "//li[contains(@class,'context-menu-icon--fa-edit')]")
edit_option.click()
time.sleep(2)

# Handle alert popup that appears after clicking "Edit"
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()  # Click OK
time.sleep(2)

