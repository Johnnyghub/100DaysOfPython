from flask import Flask, render_template
from requests import get

app = Flask(__name__)
posts = get(url='https://api.npoint.io/4af156202f984d3464c3').json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
    title = "Not found"
    subtitle = "Not found"
    body = "Not found"  # default values
    for p in posts:
        if post_id == p['id']:
            title = p['title']
            subtitle = p['subtitle']
            body = p['body']
    return render_template('post.html', title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
