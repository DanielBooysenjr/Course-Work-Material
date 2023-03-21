# Templating with Juinja in Flask Applications

from flask import Flask, render_template
import random
import datetime
import requests

AGIFY = "https://api.agify.io"
GENDERIZE = "https://api.genderize.io"



app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guessing(name):

    # Setting up API params
    params = {
    "name": f"{name}"
    }

    # Getting the age and based on name
    response = requests.get(url=AGIFY, params=params)
    response.raise_for_status()
    name = response.json()
    user_name = name["name"].capitalize()
    user_age = name["age"]

    # Getting gender based on name
    gender_response = requests.get(url=GENDERIZE, params=params)
    gender_response.raise_for_status()
    gender = gender_response.json()["gender"]
    user_gender = gender

    return render_template("name.html", name=user_name, age=user_age, gender=user_gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/3ddca80c1d4a3d82012d"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)