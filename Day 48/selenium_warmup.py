from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(url="https://www.python.org")
driver.maximize_window()

event_dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}

try:
    events = {i:{"date": event_dates[i].text, "name":event_names[i].text} for i in range(len(event_dates))}
except IndexError:
    print("Data retrieved is of different lengths, please check if HTML structure of website has been changed.")  # above code works 2022-03-02

print(events)

driver.quit()

# find element by link text > link text to click on a link on a page
# then .click() on that element to go to it

# find element by name > name of form to select a form
# search.send_keys("keys") to enter something within this form
# note, does not click enter, import keys class to do so
# need do to Keys.Enter in order to actually submit data

# if you need to click a button howveer, find the button adn then .click() on it
