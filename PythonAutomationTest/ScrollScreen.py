import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.execute_script("""
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });
""")
time.sleep(3)
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
time.sleep(3)
element = driver.find_element(By.XPATH, "//img[@title='BrowserStack']")
driver.execute_script("arguments[0].scrollIntoView(); ", element)
time.sleep(3)

scrnPath = "ScreenShotPath/sc2.png"
driver.save_screenshot(scrnPath)
time.sleep(3)
driver.quit()