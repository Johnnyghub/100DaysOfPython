from flask import Flask, render_template
import random
from requests import get
import datetime

app = Flask(__name__)
agify_api = 'https://api.agify.io/?name='
genderize_api = 'https://api.genderize.io/?name='

# use {{}} to render python code in your html file
# use {% %} for multiline python code, like for loops
# eg:
# {% for i in range(10) %}
#   <h1>{{data[i]}}</h1>  (note it is all indented)
#   <h2>{{do x with i blablabla}}}</h2>
# {% endfor %}  (denotes end of loop, while, if, etc...)


@app.route('/')
def home():
    random_num = random.randint(0, 100)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=current_year)  # send a variable to the html page
    # used when you need to import a module or have many lines of code


@app.route('/<name>')
def genderageguesser(name):
    return render_template('guess_page.html',
                           name=name,
                           gender=get(url=genderize_api+name).json()["gender"],
                           age=get(url=agify_api+name).json()["age"])


if __name__ == '__main__':
    app.run(debug=True)
