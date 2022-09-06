from bs4 import BeautifulSoup
from requests import get
from smtplib import SMTP

# can be changed to any amazon product you want to track
URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463'
preset_price = 200  # check against this price

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70",
    "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8",
}

with get(url=URL, headers=HEADERS) as response:
    soup = BeautifulSoup(response.text, 'html.parser')

price = int(soup.find(name='span', class_='a-offscreen').string[1:])  #remove dollar sign and turn into int
# sometimes it is buggy and returns a captcha page

if price < preset_price:
    my_email = "johnnyscsgosmurf@hotmail.com"  # this email is sometimes locked due to always being used for SMTP
    # if error 535, manually unlock

    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="throwAway2022")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="johnnymorcos02@gmail.com",
            msg=f"Subject:Item you're interested in is at a good price!\n\nAn item you are following on Amazon is "
                f"currently priced below your preset price point.\nFollow this link to purchase it: {URL}."
        )
