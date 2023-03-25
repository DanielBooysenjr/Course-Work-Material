from flask import Flask, render_template
from form import MyForm

app = Flask(__name__)

app.secret_key = '140-284-680'

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login_page():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)