import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

element_to_hover = driver.find_element(By.XPATH, "(//span[contains(text(),'Fashion')]/../../../../..//following-sibling::div)[1]")
actions = ActionChains(driver)
time.sleep(5)
actions.move_to_element(element_to_hover).perform()

wait =WebDriverWait(driver, 10)
footwear= wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Men Footwear']")))
actions.context_click(footwear).perform()
time.sleep(2)
actions.send_keys('t').perform()
driver.save_screenshot("ScreenShotFolder/ScreenShot2.jpg")



