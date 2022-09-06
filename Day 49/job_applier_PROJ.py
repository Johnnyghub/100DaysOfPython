from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# need to setup linked in account
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""

chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(5)
driver.find_element(by=By.LINK_TEXT, value="Sign in").click()

time.sleep(5)
driver.find_element(by=By.ID, value="username").send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(3)
    try:
        driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button").click()

        time.sleep(5)
        phone = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()
            
            time.sleep(3)
            driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1].click()
            print("Complex application. Skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(3)
        driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss").click()

    except NoSuchElementException:
        print("No application button. Skipped.")
        continue

time.sleep(5)
driver.quit()

