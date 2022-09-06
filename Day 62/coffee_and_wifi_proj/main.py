from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def append_data(cafe, location, open_time, close_time, coffee, wifi, power):
    data = f"{cafe},{location},{open_time},{close_time},{coffee},{wifi},{power}"
    f = open("cafe-data.csv", "a", encoding="utf-8")
    f.write(f"{data}\n")
    f.close()


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location_url = StringField(label='Location', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open Time', validators=[DataRequired()])
    close_time = StringField(label='Close Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee',choices=["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi', choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField(label='Power', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        append_data(form.cafe.data, form.location_url.data, form.open_time.data, form.close_time.data, form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data)
        return render_template('index.html')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
