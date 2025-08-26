import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open("DataSet/Data1.txt") as f:
    lines = f.readlines()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait =WebDriverWait(driver, 10)

for line in lines:
    userName, passWord = line.strip().split(", ")
    print("Testing with ", userName, passWord)

    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys(userName)
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).clear()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys(passWord)
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Login']"))).click()
    time.sleep(2)

    try:
        logoutMenu = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-userdropdown-tab']")))
        logoutMenu.click()
        logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()
        time.sleep(2)

    except:
        print("Login failed for:", userName)


driver.quit()