from typing import Callable
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fhraeiug32453278#@#@19'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class MySQLAlchemy(SQLAlchemy):  # IDE does not recognize SQLAlchemy types as callable so use this to bypass, may not work depending on version
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable
    Model: Callable


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        # ignore unexpected argument error if it shows, it is an issue with the PyCharm IDE or whatever IDE is being used to view this code, not the code.
        user_to_add = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
            # if you want to remove the method$salt part of the password use, but this breaks login => .split("$")[2]
        )

        db.session.add(user_to_add)
        db.session.commit()

        login_user(user_to_add)

        return redirect(url_for('secrets', name=user_to_add.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  # email is a unique identifier

        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))

        if check_password_hash(user.password, password):  # compares the hashes of the stored and entered passwords for security
            login_user(user)
            return redirect(url_for('secrets', name=user.name))
        else:
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))

        # NOTE: for security purposes, never display what is exactly wrong with a certain login, simply say invalid credentials
        # Specifying the part that is incorrect will lead hackers to hack accounts faster
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)  # pass name from redirect, because we don't want it to show up in the URL


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.static_folder, path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
