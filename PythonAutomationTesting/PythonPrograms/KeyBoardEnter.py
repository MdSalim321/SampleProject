import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
ac = ActionChains(driver)

# mouse action
wait = WebDriverWait(driver, 20)
search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Search for Products, Brands and More')]")))
ac.move_to_element(search).perform()
time.sleep(4)

# Now Keyboard data input
search.send_keys("Footwear")
time.sleep(4)
search.send_keys(keys.ENTER)


