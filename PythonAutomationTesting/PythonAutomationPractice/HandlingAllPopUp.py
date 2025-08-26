import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open demo site
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# Locate the right-click button
right_click_button = driver.find_element(By.XPATH, "//span[text()='right click me']")

actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

# Get total menu items dynamically (count)
actions.context_click(right_click_button).perform()
menu_items = driver.find_elements(By.CSS_SELECTOR, "ul.context-menu-list li.context-menu-item")
total_items = len(menu_items)
print("Total Menu Items Found:", total_items)

# Loop through menu items by index
for i in range(total_items):
    # Right click each time (because menu disappears after selection)
    actions.context_click(right_click_button).perform()

    # Fetch fresh menu items every time
    menu_items = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.context-menu-list li.context-menu-item"))
    )

    # Click on the i-th item
    item_text = menu_items[i].text
    print("Clicking on:", item_text)
    menu_items[i].click()

    # Handle alert popup
    alert = wait.until(EC.alert_is_present())
    print("Alert Text:", alert.text)
    alert.accept()
    time.sleep(1)

driver.quit()
