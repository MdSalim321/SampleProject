from selenium import webdriver
driver = webdriver.Chrome()


driver.get("https://www.facebook.com/")
driver.save_screenshot("ScreenShotFolder/ScreenShot2.jpg")
