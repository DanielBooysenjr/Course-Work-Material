from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import SubmitField, TelField
from wtforms.validators import DataRequired
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

API = 'YOUR API'
READ_ACCESS = 'YOUR READ ACCESS CODE'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///favorite-movies.db'
db = SQLAlchemy(app)

class MOVIES(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column (db.String, unique=True, nullable=True)
    img_url = db.Column (db.String, unique=True, nullable=False)

with app.app_context():
    db.create_all()


class EditMovie(FlaskForm):
    rating = TelField("New Rating eg. 8.4", validators=[DataRequired()])
    review = StringField("New Review", validators=[DataRequired()])
    submit = SubmitField("Submit")

class AddMovie(FlaskForm):
    movie_name = StringField("Name of new movie", validators=[DataRequired()])
    search = SubmitField("Add Movie")

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
img_url = 'https://image.tmdb.org/t/p/w500/'
movies_list = []

@app.route("/")
def home():
    num = 0
    movies = MOVIES.query.order_by(desc(MOVIES.rating)).all()
    pos = request.args.get('pos')
    try:
        index = int(pos)
        title = movies_list[0][index]['title']
        year = movies_list[0][index]['release_date']
        description = movies_list[0][index]['overview']
        url = movies_list[0][index]['poster_path']
        img = img_url + url
        new_movie = MOVIES(title=title, year=year, description=description, img_url=img)
        db.session.add(new_movie)
        db.session.commit()
        db.session.rollback()
        movies_list.clear()
        return redirect(url_for('home'))
    except Exception as e:
        print(e)

    return render_template("index.html", movies=movies, num=num)


@app.route('/edit/<int:num>', methods=['POST', 'GET'])
def edit(num):
    form = EditMovie()
    movie = MOVIES.query.filter_by(id=num).first()  # get the movie based on the id in the URL


    if form.validate_on_submit():
        # movie_count = MOVIES.query.count()
        # num = movie_count 
        new_data = form.data
        new_rating = new_data['rating']
        new_review = new_data['review']
        movie = MOVIES.query.filter_by(id=num).first()
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for('home'))
    pos = request.args.get('pos')
    return render_template("edit.html", form=form, num=pos)


@app.route('/delete/<int:num>')
def delete(num):
    movie = MOVIES.query.filter_by(id=num).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add-movie', methods=['POST', 'GET'])
def add_movie():
    add = AddMovie()
    return render_template("add.html", add=add)


@app.route('/results', methods=['POST', 'GET'])
def results():
    add = AddMovie()
    movie = add.data
    new_movie_name = movie['movie_name']
    
    params = {
        'api_key': API,
        "query": new_movie_name
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie?", params=params)
    response.raise_for_status()
    data = response.json()
    all_movies = data['results']
    movies_list.append(all_movies)
    pos = 0
    # movie_count = MOVIES.query.count()
    # num = movie_count + 1

    
    return render_template('select.html', title=all_movies, pos=pos, num=pos)


if __name__ == '__main__':
    app.run(debug=True)
