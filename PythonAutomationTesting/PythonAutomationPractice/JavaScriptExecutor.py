import time
from selenium import webdriver

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")

# Create JavaScript alert
driver.execute_script("alert('This is a test alert!');")
time.sleep(2)

# Switch and accept alert
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.accept()
time.sleep(2)

# Create JavaScript confirm popup
driver.execute_script("confirm('Do you want to continue?');")
time.sleep(2)

alert = driver.switch_to.alert
print("Confirm Text:", alert.text)
alert.dismiss()   # Clicks Cancel
time.sleep(2)

# Create JavaScript prompt
driver.execute_script("prompt('Enter your name:','Selenium User');")
time.sleep(2)

alert = driver.switch_to.alert
print("Prompt Text:", alert.text)
alert.send_keys("Admin")
alert.accept()   # Clicks OK

time.sleep(3)
driver.quit()
