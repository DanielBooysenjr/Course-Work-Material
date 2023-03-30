import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books.db'

db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

with app.app_context():
    db.create_all()
    data = Books(id=1, book="Harry Potter", author="JK Rowling", rating=4.6)
    db.session.add(data)
    db.session.commit()

# db = sqlite3.connect("Books-Collection.db")
# cursor = db.cursor()

# cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar (250) NOT NULL, rating FLOAT NOT NULL)')