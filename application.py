import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/my_activities")
def activities():
    return render_template("my_activities.html")

@app.route("/friends")
def friends():
    pictures = ["sanne_linde.jpg", "julia.jpg","alva.jpg", "emilie.jpg","kira_lea.jpg"]
    return render_template("friends.html", pictures=pictures)

@app.route("/family")
def family():

    return render_template("family.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/birthday")
def birthday():
    now = datetime.datetime.now()
    my_birthday = now.month == 12 and now.day == 24
    return render_template("birthday.html", my_birthday = my_birthday)

@app.route("/my_memoirs", methods=["POST", "GET"])
def my_memoirs():
    if session.get("memoirs") is None:
        session["memoirs"] = []
    if request.method == "POST":
        story = request.form.get("story")
        session["memoirs"].append(story)

    return render_template("my_memoirs.html", memoirs=session["memoirs"])
