from flask import Flask, render_template
from forms import LoginForm
from datetime import datetime
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret_key'


def append_data(email, password, success):
    login_data = {"email":email, "password":password, "time":f"{datetime.now()}", "success":success}
    f = open("login_history.txt", "a")
    f.write(f"{login_data}\n")
    f.close()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data == "admin@email.com") & (form.password.data == "12345678"):
            append_data(form.email.data, form.password.data, "success")
            return render_template('success.html')
        else:
            append_data(form.email.data, form.password.data, "denied")
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    