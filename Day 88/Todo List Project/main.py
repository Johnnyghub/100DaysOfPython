import datetime
from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

tasks = []  # this program is meant to refresh daily so we can just locally store the task array for now


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        task = request.form['task']
        complete = False  # tasks are always not complete by default
        tasks.append([task, complete])
        return redirect(url_for('home'))
    return render_template("index.html", todays_date=datetime.date.today(), tasks=tasks)


@app.route("/check-task/<index>", methods=['GET', 'POST'])
def check_task(index):
    if request.method == "POST":
        if request.form['task_done'] == 'True':
            tasks[int(index)][1] = True  # save whether or not the box is checked so it persists on reload
        else:
            tasks[int(index)][1] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
