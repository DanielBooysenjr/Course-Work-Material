from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def submission():
    if request.method == "POST":
        email = request.form["mail"]
        password = request.form["password"]
        return render_template("login.html", email=email, password=password)
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)