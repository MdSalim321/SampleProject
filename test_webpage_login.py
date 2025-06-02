import time
import pytest
from selenium import webdriver

def test_google():

   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get("https://www.google.com/")
   assert driver.title == "Google"
   driver.quit()

def test_facebook():

   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get("https://www.facebook.com/")
   title_actual = driver.title
   title_expected = "Facebook – log in or sign up"
   assert title_actual == title_expected, "title does not matched"
   driver.quit()

def test_instagram():

   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get("https://www.instagram.com/")
   assert driver.title == "Instagram"
   driver.quit()

def test_rediff():

   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get("https://www.rediff.com/")
   assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"
   driver.quit()


