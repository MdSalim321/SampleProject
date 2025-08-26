import os.path
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
driver.implicitly_wait(10)

# choose file
# filePath = os.path.abspath("D:/Selenium Documents/Test.pdf")
base_dir = os.path.dirname(os.path.abspath(__file__))

baseDir = os.path.dirname(os.path.abspath(__file__))
relativePath = os.path.join(baseDir, "DataSheet", "Test.pdf")

print(base_dir)
time.sleep(3)
filePathRelative = os.path.join(base_dir, "DataSheet", "Test.pdf")
print(filePathRelative)
time.sleep(3)

time.sleep(3)
chooseFile = driver.find_element(By.XPATH, "//input[contains(@id, 'file-upload')]")
time.sleep(3)
chooseFile.send_keys(filePathRelative)
# UPload file
time.sleep(3)
driver.find_element(By.XPATH, "//input[contains(@id, 'file-submit')]").click()
time.sleep(3)



