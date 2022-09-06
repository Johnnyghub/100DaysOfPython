from data_scraper import get_top_n_trending_games
from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
import random as rand  # there is a conflict since there is a view called random.py, thus import as rand

# This program transforms the day 92 web scraper to return the data it gets using an API instead of appending to file

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html", static='static')


@app.route("/return_n_games", methods=['POST', 'GET'])
def return_n_games():
    if request.method == "POST":
        trending_games = get_top_n_trending_games(int(request.form['n']))
        return trending_games
    return {'URLError': 'Add the number of games you want to return to the URL with /n or go through the main page of the site'}  # use other route message


@app.route("/get_games/<n>")  # this method if the user wants to use the API in a program, where they need an endpoint and can't go through the homepage
def get_games(n):
    try:
        trending_games = get_top_n_trending_games(int(n))
    except:
        return {'TypeError': 'Please enter an integer betweeen 1-50'}
    return trending_games


@app.route("/return_random_game", methods=['POST', 'GET'])  # not much point to this method, kind of costly for no reason, consider removing
def return_random_game():
    trending_game = rand.choice(get_top_n_trending_games(50))
    return trending_game


if __name__ == '__main__':
    app.run(debug=True)

