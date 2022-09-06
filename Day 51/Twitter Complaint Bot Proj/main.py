from internet_speed_twitter_bot import InternetSpeedTwitterBot

# working as of 2022-03-06

TWITTER_AT = "100DOTBOT"
TWITTER_PASSWORD = "100DOTTwitterBot"
PROMISED_DOWN = 80
PROMISED_UP = 60
ISP_AT = "@Etisalat_Care"
chrome_driver_path = "D:\chromedriver_win32\chromedriver.exe"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_AT, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP, ISP_AT)
