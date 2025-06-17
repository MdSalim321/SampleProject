from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (Chrome example)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.google.com/")

# Wait for the page to load
time.sleep(2)

# Locate the element
element = driver.find_element(By.XPATH, "//input[@id='input']")  # Change as needed (e.g., By.CLASS_NAME, By.XPATH)

# Take a screenshot of the element
element.screenshot("ScreenShotFolder4/element_screenshot.png")

# Close the browser
driver.quit()
