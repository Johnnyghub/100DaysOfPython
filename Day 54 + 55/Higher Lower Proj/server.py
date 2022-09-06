import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0,9)


@app.route('/')
def homepage():
    return "<h1>Welcome to the higher lower game!</h1>" \
           "<h2>Guess a number between 0 and 9</h2>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def guesspage(number):
    if number < random_number:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if number > random_number:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if number == random_number:
        return "<h1 style='color:green'>You got it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
