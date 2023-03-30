from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.book}>'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['book']
        author = request.form['author']
        rating = request.form['rating']
        new_book = Books(book=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

    all_books = Books.query.all()

    return render_template("index.html", books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    return render_template("add.html")

@app.route("/edit/<int:num>", methods=['POST', 'GET'])
def edit(num):
    # Query specific row and getting specific info
    book_to_edit = Books.query.filter_by(id=num).first()
    # Assigning Variables
    author = book_to_edit.author
    book = book_to_edit.book
    rating = book_to_edit.rating
    if request.method == "POST":
        book_to_edit = Books.query.filter_by(id=num).first()
        new_rating = request.form['new-rating']
        book_to_edit.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", books=book_to_edit, num=num, author=author, book=book, rating=rating)




if __name__ == "__main__":
    app.run(debug=True)
