from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class AptDataBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("D:\chromedriver_win32\chromedriver.exe"))
        self.form_url = 'https://forms.gle/mQXkSbMLtbNTNg6UA'
        self.zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3Anull%2C"mapBounds"%3A%7B"west"%3A-122.56276167822266%2C"east"%3A-122.30389632177734%2C"south"%3A37.69261345230467%2C"north"%3A37.857877098316834%7D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fr"%3A%7B"value"%3Atrue%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"pmf"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"max"%3A3000%7D%2C"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12%7D'
        self.headers = {  # avoid captcha
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70",
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'upgrade-insecure-requests': '1',
        }
        self.data = []

    def get_apt_data(self):
        """Gets the data of the first page of apartment listings on Zillow. Zillow uses anti web scraping measures on
        their site so we use selenium to get around that."""

        with get(url=self.zillow_url, headers=self.headers) as response:
            soup = BeautifulSoup(response.text, 'html.parser')

            for ul in soup.find_all(name='ul', class_='photo-cards'):  # create a dictionary with data we actually want
                for listing in ul.find_all(name='li'):
                    try:
                        link = listing.find(name='a', class_='list-card-link').get("href")
                        if link[0] == '/':  # if it is a partial link, sometimes used for no reason
                            link = 'https://www.zillow.com' + link  # turn it into a functional link

                        self.data.append({
                            'price': listing.find(name='div', class_='list-card-price').getText().split('+')[0].split('/')[0],  # split by + for bedrooms then / for month
                            'address': listing.find(name='address', class_='list-card-addr').getText(),
                            'link':link,
                        })
                    except AttributeError:
                        pass  # this means the li child was deleted on the webpage and the html tags are still there as far as I can tell

    def enter_data_to_form(self):
        """Opens the link to the google form I made that will then allow me to move the data to an excel file easily
        after selenium inputs the data into the fields for me."""
        self.driver.get(self.form_url)
        for data in self.data:
            time.sleep(3)  # so the page has time to load
            fields = self.driver.find_elements(by=By.CSS_SELECTOR, value='.whsOnd.zHQkBf')  #gives all 3 fields
            fields[0].send_keys(data['address'])
            fields[1].send_keys(data['price'])
            fields[2].send_keys(data['link'])

            self.driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
            # submit button

            time.sleep(3)
            self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
            # click submit another response button

        self.driver.quit()
