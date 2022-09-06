import csv
import json
import pprint
from datetime import datetime
from bs4 import BeautifulSoup
from requests import get

# Works as of June 14 2022

"""This program scrapes the steam 250 site to get the current top 20 trending games based on review velocity, which is
the number of reviews per day, regardless of whether they are positive or negative. This can be useful to see which games 
are currently best to write articles about. Also gets other various related data."""

URL = "https://steam250.com/trending"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}  # prevents access denied

with get(url=URL, headers=headers) as response:
    soup = BeautifulSoup(response.content, 'html.parser')

top_20_trending_games = []  # will be in order from most trending to least trending

for i in range(1,21):  # the site marks each of their entries with an id='index' where index is the current position in the rankings
    temp = soup.find(id=i)

    # --------- get the title -----------

    try:
        title = temp.find('span', class_='title').get_text()  # get the text but it will include the ranking number

        if i < 10:  # if ranking is single digit:
            title = title[4:]  # remove the first 3 characters, eg: "1. " to get only the title
        else:
            title = title[5:]  # remove the first 4 characters, eg: "11. " to get only the
    except:
        title = 'No Title Could Be Retrieved'  # just in case the game does not have a title

    # -------- get the price ------------

    try:
        price = temp.find('span', class_='price').get_text()
    except TypeError:  # free games do not have a price tag and return None, which cannot be stripped, so:
        price = '$0.00'
    except AttributeError:
        price = '$0.00'

    # ---------- get the link -----------

    try:
        link = temp.find('a', class_='store')['href'][:-1]  # get the href link and remove the \n at the end of the link
    except:
        link = 'No Link Could Be Retrieved'  # in case the steam page no longer exists or some such occurence

    # --------- get the review velocity ---------

    try:
        review_velocity = temp.find('span', class_='velocity').get_text()
        review_velocity = review_velocity.split(" ")[1]  # remove the word velocity and get only the value
        review_velocity = review_velocity.replace(",", "")  # for review velocities over 999, remove the comma so we can turn it into an integer
        review_velocity = int(review_velocity)  # cast to an int
    except:
        review_velocity = "Data Unavailable"

    # ----------- get the rating ------------

    try:
        rating = temp.find('span', class_='rating').get_text()
        rating = rating.split(" ")[1]  # remove the word 'rated' and get only the percentage
    except:
        rating = 'No Ratings'  # shouldn't happen... but in the case that a developer or steam deleted all reviews, review velocity wouldn't change but rating would have no value

    entry = {
        'game_name': title,
        'current_price': price,
        'steam_link': link,
        'review_velocity': review_velocity,
        'rating': rating
    }

    top_20_trending_games.append(entry)

cols = ['game_name', 'current_price', 'steam_link', 'review_velocity', 'rating']  # to pass to dictwriter
todays_date = datetime.today()  # so we don't call datetime 3 times

with open(f'./scraped_data/data_{todays_date.day}_{todays_date.month}_{todays_date.year}.csv', 'w', encoding='UTF-8', newline='') as file:  # file named after today's date
    writer = csv.DictWriter(file, fieldnames=cols)
    writer.writeheader()
    writer.writerows(top_20_trending_games)

# also save the data as a json file and add the ranking as the key to each entry

top_20_json = {i+1: top_20_trending_games[i] for i in range(len(top_20_trending_games))}

with open(f'./scraped_data/data_{todays_date.day}_{todays_date.month}_{todays_date.year}.json', 'w') as file:  # file named after today's date as well
    json.dump(top_20_json, file, ensure_ascii=False, indent=4)

