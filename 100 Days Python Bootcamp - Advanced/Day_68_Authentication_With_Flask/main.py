from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
file_folder = 'static/files'


app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('login.html')
        except:
            flash("User with that email address already registerd, please login instead.")
            return render_template('login.html')
    return render_template("register.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            name = user.name
            print(name)
            if user and check_password_hash(user.password, password):
                login_user(user)
                return render_template('secrets.html', user=name)
    except:
        if User.query.filter_by(email=email).first():
            flash("Please check your username and password")
        else:
            flash("No user registered with that email.\n\nPlease create an account first.")
        return render_template('login.html')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        file_folder, 'cheat_sheet.pdf'
    )


if __name__ == "__main__":
    app.run(debug=True)
