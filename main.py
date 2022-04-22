import os
from flask import Flask, render_template, url_for, request

from classes import *

app = Flask(__name__)

@app.route("/")
def render_main_page():
    return render_template("index.html")


@app.route("/lessons")
def render_first_game():
    return render_template("lessons.html")


@app.route("/lessons/1")
def render_lessons_page():
    return render_template("game_1.html")


@app.route("/lessons/2")
def render_second_game():
    return render_template("game_2.html")


@app.route("/register")
def render_register():
    return render_template("registration.html")


@app.route("/login")
def render_login():
    return render_template("autorization.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)