import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, WebDriverException
from urllib3.exceptions import NewConnectionError, MaxRetryError

import text_to_int
import threading

chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(url="https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()  # avoid not being able to click things due to them being offscreen

cookie_found = False  # incase of long loading times
cookie = None

while not cookie_found:  # loop until cookie is found
    try:
        time.sleep(5)  # give page time to load
        cookie = driver.find_element(by=By.ID, value="bigCookie")
    except:
        pass
    else:
        cookie_found = True


def checkForUpgrades():
    """Every 2 seconds, check if there are available upgrades. If there are, purchase the most expensive one
    Crates however, take priority, so program will always buy the cheapest available crate before any upgrades
    since they have the largest impact."""
    try:
        threading.Timer(2.0, checkForUpgrades).start()  # every 2 seconds
        crates = driver.find_elements(by=By.CSS_SELECTOR, value="#upgrades .crate.enabled")

        if len(crates) == 0:  # there are no crates to purchase, they take priority
            upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store .product.enabled")
            prices = [int(text_to_int.text2int(upgrade.text.split('\n')[1].lower())) for upgrade in upgrades]
            # text to int needed because some prices have words such as million/billion/etc in them
            if len(prices) != 0:
                try:
                    upgrades[prices.index(max(prices))].click()  # select most expensive upgrade and click it
                except ElementClickInterceptedException:
                    print("Element click intercepted by something else. Skipping this round of upgrades.\n")
                except StaleElementReferenceException:
                    print("Element is off the screen or something.\n")
        else:
            crates[0].click()  # for crates, always buy the first one
    except WebDriverException:
        quit()  # program over, end threading
    except ConnectionRefusedError:
        quit()
    except NewConnectionError:
        quit()
    except MaxRetryError:
        quit()


checkForUpgrades()

timeout = time.time() + 60*5  # stop running in 5 minutes
play = True
cps = 0

while play:
    cookie.click()
    if time.time() > timeout:
        play = False
        try:
            print(f"You achieved cookies {driver.find_element(by=By.CSS_SELECTOR, value='#cookies div').text} in 5 minutes.")
        except StaleElementReferenceException:  # for some reason when running the program, it decides 'no, can't find this, bye' and crashes
            pass

driver.quit()
quit()
