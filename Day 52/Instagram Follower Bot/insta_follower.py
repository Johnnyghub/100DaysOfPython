from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# MAIN FLAW: This program ends up limiting the user after a bunch of follows because the account is presumably going to be brand new
# Try to use the account normally for a while before running this to avoid being temporarily locked


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("D:\chromedriver_win32\chromedriver.exe"))

    def login(self, username, password):
        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(3)
        username_input = self.driver.find_element(by=By.NAME, value='username')
        username_input.send_keys(username)

        password_input = self.driver.find_element(by=By.NAME, value='password')
        password_input.send_keys(password + Keys.ENTER)

        time.sleep(5)

    def find_followers(self, account, number_of_follows_required):
        self.driver.get(f'https://www.instagram.com/{account}/')  # link to account is link/account/ always, can do this for convenience

        time.sleep(3)

        # sometimes when loading the account page, we get an HTML error of 560, refreshing the page seems to fix this
        # cause is unknown
        try:
            self.driver.find_element(by=By.XPATH, value='//a[@href="' + '/chefsteps/followers/' + '"]').click()  # find follower button by href value
        except NoSuchElementException:
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('r').key_up(Keys.CONTROL).perform()  # refresh page

        time.sleep(3)
        follower_popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')

        for i in range(number_of_follows_required // 15):  # each scroll is roughly 15 people, floor division this to get range
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)
            time.sleep(2)  # loading time

    def follow(self):
        follower_popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
        follow_buttons = follower_popup.find_elements(by=By.CSS_SELECTOR, value='button.sqdOP')  # get all follow buttons
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                time.sleep(1)  # to seem more human
            except ElementClickInterceptedException:  # incase already following this user, click cancel button
                cancel_button = self.driver.find_element(by=By.CLASS_NAME, value='HoLwm')
                cancel_button.click()
                time.sleep(1)
                follow_button.click()  # or else it will skip a user
                time.sleep(1)
