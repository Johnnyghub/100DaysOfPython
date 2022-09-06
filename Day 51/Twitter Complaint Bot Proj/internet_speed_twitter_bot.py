from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("D:\chromedriver_win32\chromedriver.exe"))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('r').key_up(Keys.CONTROL).perform()  # speedtest driver just loads infinitely otherwise
        # sometimes no matter what you do speedtest decides to load forever and no actions get taken, can fix by clicking stop load manually only
        # TODO: Add javascript command to force window to stop loading to avoid this issue
        go_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".speedtest-container.main-row a")
        go_button.click()
        no_results_yet = True

        time.sleep(15)
        while no_results_yet:  # try every 15 seconds to get the results because the test takes time to complete
            try:
                self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)
                self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)

                if (self.down != " ") and (self.up != " "):
                    no_results_yet = False
                else:
                    time.sleep(15)
            except:  # if the elements aren't even found, or any error occurs
                time.sleep(15)  # wait 15 seconds

        print(f"Internet speed: {self.down} down/{self.up} up Mbps")

        self.driver.delete_all_cookies()
        self.driver.quit()

    def tweet_at_provider(self, at, password, promised_down, promised_up, isp_at):
        if (self.up < promised_up) or (self.down < promised_down):  # if internet speeds lower than anticipated
            self.driver = webdriver.Chrome(service=Service("D:\chromedriver_win32\chromedriver.exe"))
            # recreate the driver to avoid newconnectionerror
            self.driver.get("https://www.twitter.com/")
            time.sleep(5)  # time for site to load
            try:
                sign_up_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
            except NoSuchElementException:  # incase a different version of twitter is loaded, still finds element
                sign_up_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[2]/div[4]/div[2]')

            sign_up_button.click()

            time.sleep(3)
            at_form = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
            at_form.send_keys(at + Keys.ENTER)

            time.sleep(3)
            password_form = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_form.send_keys(password + Keys.ENTER)

            time.sleep(5)
            tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            tweet_button.click()

            time.sleep(2)
            ActionChains(self.driver).send_keys(f"Hi {isp_at}, why is my internet speed {self.down} down/{self.up} up Mbps when I pay for {promised_down} down/{promised_up} up Mbps?").perform()

            time.sleep(2)
            tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
            tweet_button.click()

            time.sleep(5)  # makes sure the tweet sends

            self.driver.quit()
        else:
            print("Internet speeds within accepted limits :)... for now.")

