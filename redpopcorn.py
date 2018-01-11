

# main app

from flask import Flask
from flask import render_template,request
from indicer import MovieIndexer,load_movies

app = Flask(__name__)


def get_movies(search):
    movies = load_movies()
    corn = MovieIndexer(movies)
    heat_corn = list(corn.split_for_clarity())
    found_movies = list(corn.find_movie(heat_corn,search))
    return found_movies

@app.route("/",methods=['GET'])
def index():
    movie_list = get_movies("lol")
    return render_template("home.html",movies=movie_list)

if __name__ == "__main__":
    app.run(port=5000,debug=True)
