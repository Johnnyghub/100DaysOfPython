from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, URL
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable


db = SQLAlchemy(app)


# unresolved attribute reference may show up, but the code will still work, pycharm bug
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(500), nullable=False)


db.create_all()

# test
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=1,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


class MovieRatingForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddMovieForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    year = IntegerField(label='Year', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()  # order movies by rating

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i  # this sets the ranking of each movie as their position in the array minus 1
    db.session.commit()
    return render_template('index.html', movies=all_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        # ranking = 0 is a filler value
        new_movie = Movie(title=form.title.data, year=form.year.data, description=form.description.data, rating=form.rating.data, ranking=0, review=form.review.data, img_url=form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MovieRatingForm()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_to_delete = Movie.query.get(request.args.get('id'))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
