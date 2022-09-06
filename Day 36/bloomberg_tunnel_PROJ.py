from requests import get
from smtplib import SMTP

# AlphaVantage
AV_API_KEY = "FM96R562VDNQ8MFN"
FUNCTION = 'TIME_SERIES_DAILY'
STOCK = "TSLA"

# News API
NEWS_API_KEY = "6c14d1361f094e85802a3999c297b0ed"
COMPANY_NAME = "Tesla Inc"

# turns data into indexable list, 0 is yesterdays closing price, 1 is before yesterday's closing price in USD
with get(f"https://www.alphavantage.co/query?function={FUNCTION}&symbol={STOCK}&apikey={AV_API_KEY}") as response:
    stock_data = [float(value['4. close']) for (key, value) in response.json()['Time Series (Daily)'].items()][:2]

percentage_difference = round((abs(stock_data[0]-stock_data[1]) / stock_data[0]) * 100, 2)
if stock_data[0] > stock_data[1]:
    symbol = '🔺'
else:
    symbol = '🔻'


# if a significant percentage difference in stock price, return 3 most recent articles, filter to only title, brief & url
if percentage_difference >= 3:
    with get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}") as response:
        articles = [{'title': data['title'], 'brief': data['description'], 'url': data['url']} for data in response.json()["articles"][:3]]

    email_content = f"Subject:Fluctuation in {STOCK}\n\n{STOCK}: {symbol}{percentage_difference}%\n" \
                    f"The closing value of {STOCK} has changed dramatically in the last 2 days, check your portfolio " \
                    f"to see if you would like to purchase more or sell.\nHere are some related articles to this company:" \
                    f"\n\nTitle: {articles[0]['title']}\nBrief: {articles[0]['brief']}\nRead more: {articles[0]['url']}" \
                    f"\n\nTitle: {articles[1]['title']}\nBrief: {articles[1]['brief']}\nRead more: {articles[1]['url']}" \
                    f"\n\nTitle: {articles[2]['title']}\nBrief: {articles[2]['brief']}\nRead more: {articles[2]['url']}"

    my_email = "johnnyscsgosmurf@hotmail.com"

    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="throwAway2022")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="johnnym2002@hotmail.com",
            msg=email_content.encode('utf-8')
        )
