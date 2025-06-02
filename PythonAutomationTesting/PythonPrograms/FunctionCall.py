import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def Greeting():
    print("Hello world")
    print("I am staring writing the python programmin language")

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)



    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.google.com/")

    Wait =WebDriverWait(driver, 10)
    textBox= Wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    textBox.send_keys("facebook")
    time.sleep(5)
    textBox.send_keys(Keys.ENTER)

Greeting()