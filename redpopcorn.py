

# main app

from flask import Flask
from flask import render_template,request,redirect
from indicer import MovieIndexer,load_movies
import random

app = Flask(__name__)


def get_movies(search):
    movies = load_movies()
    corn = MovieIndexer(movies)
    heat_corn = list(corn.split_for_clarity())
    found_movies = list(corn.find_movie(heat_corn,search))
    return found_movies

@app.route("/")
def index():
    cur_url = request.url_rule
    print(cur_url)
    return render_template("home.html",movies=[],current_url=cur_url)

@app.route('/popcorns',methods=["POST"])
def show_popcorns():
    if request.method == "POST":
        movie_name = request.form['search_box']
        movie_list = get_movies(movie_name)
        if movie_list:
            cur_url = request.url_rule
            return render_template("show_movies.html",movies=movie_list,search_text = movie_name,current_url =cur_url)
        return render_template("movie_not_found.html",error_text="Sorry could'nt find any movie")
    return redirect(url_for('index'))


if __name__ == "__main__":
    port_num = random.randint(2000,9999)
    try:
        app.run(port=port_num,debug=True)
    except OSError:
        app.run(port=port_num+1,debug=True)
