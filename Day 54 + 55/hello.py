from flask import Flask
app = Flask(__name__)

# cd "Day 54" after opening venv, or else won't work, make sure to cd to the folder the file is contained
# set FLASK_APP=hello.py
# flask run
# in order to run this file, same syntax in general
# Consider setting the file in the terminal settings because this technique requires you to redo it everytime you
# open the terminal


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Welcome to my site.</p>' \
           '<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Ficatcare.org%2Fadvice%2Fthinking-of-getting-a-cat%2F&psig=AOvVaw3niRqjzZck7nRx5SKdIHoU&ust=1646781187475000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCIih2I-QtfYCFQAAAAAdAAAAABAD">'


def make_bold(function):
    def wrapper_function(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"
    return wrapper_function


def make_italic(function):
    def wrapper_function(*args, **kwargs):
        return f"<em>{function(*args, **kwargs)}</em>"
    return wrapper_function


@app.route('/bye')
@make_bold
@make_underlined
@make_italic
def bye():
    return "Bye!"


@app.route('/<name>')  # variables between <>
def greet(name):
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run(debug=True)
