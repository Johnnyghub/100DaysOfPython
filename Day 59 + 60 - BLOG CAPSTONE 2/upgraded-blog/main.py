from flask import Flask, render_template, url_for, request
from smtplib import SMTP
import requests

app = Flask(__name__)

endpoint = 'https://api.npoint.io/a15a067b527ab90c09b3'
posts = requests.get(endpoint).json()


@app.route('/')
def home():
    return render_template("index.html", static=url_for("static", filename=""), data=posts)


@app.route("/about")
def about():
    return render_template("about.html", static=url_for("static", filename=""))


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["phone"], data["email"], data["message"])
        return render_template("contact.html", static=url_for("static", filename=""), messageSent=True)
    else:
        return render_template("contact.html", static=url_for("static", filename=""), messageSent=False)


def send_email(name, phone, email, msg):
    message = f"Subject:New Message From Blog\n\nName: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {msg}"
    my_email = "johnnyscsgosmurf@hotmail.com"

    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="throwAway2022")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="johnnym2002@hotmail.com",
            msg=message.encode('utf-8')
        )


@app.route("/<int:index>")
def post(index):
    this_post = None
    for post_data in posts:
        if post_data["id"] == index:
            this_post = post_data
    return render_template("post.html", post=this_post)


if __name__ == '__main__':
    app.run(debug=True)
