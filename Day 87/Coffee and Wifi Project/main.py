from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Turns the cafe data into a dictionary with dictionary comprehension rather than writing out the entire
        dictionary when you turn it into JSON data to output with the API. column refers to a column in relation to
        that specific table entry, and then getattr returns the value associated with that specific entry in that column.
        __table__ is a way to access the current table with SQLAlchemy."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# only needed once or when changes are made
# db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    cafes_list = Cafe.query.all()  # read all data
    return render_template('cafes.html', cafes=cafes_list)


if __name__ == '__main__':
    app.run(debug=True)
