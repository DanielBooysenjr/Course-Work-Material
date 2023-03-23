# Creating a blog
from flask import Flask, render_template
import requests

ENDPOINT = 'https://api.npoint.io/9422a4b6657a01c00f7f'

response = requests.get(ENDPOINT)
posts = response.json()


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html", post=posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post(num):
    return render_template('post.html', post=posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)