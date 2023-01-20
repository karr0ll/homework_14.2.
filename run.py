from flask import Flask, jsonify
from flask import Blueprint

from gengre_data import get_genre
from movie_data import get_movie_data
from release_date_data import get_release_date_interval
from rating_data import get_rating

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False


@app.route("/")
def page_index():
    return "Это главная страница"


@app.route("/movie/<title>")
def load_movie_data(title):
    data = get_movie_data(title)
    return data

@app.route("/movie/<int:year_from>/to/<int:year_to>")
def load_release_date_data(year_from, year_to):
    data = get_release_date_interval(year_from, year_to)
    return data

@app.route("/rating/<rating>")
def load_movies_rating(rating):
    data = get_rating(rating)
    return data

@app.route("/genre/<genre>")
def load_movies_by_genre(genre):
    data = get_genre(genre)
    return data

if __name__ == "__main__":
    app.run()
