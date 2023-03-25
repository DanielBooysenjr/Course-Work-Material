# Creating a blog
from flask import Flask, render_template, request
import requests
import smtplib
my_email = "YOUR EMAIL"
my_password = "YOUR PASSWORD"


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

@app.route('/contact', methods=['POST', 'GET'])
def information():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["useremail"]
        phone = request.form["userphone"]
        message = request.form["usermessage"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: New Message\n\n Name: {name}, Email: {email}, Phone: {phone}\nMessage: {message}"
            )
        return f"<h1>Message sent</h1>"
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)