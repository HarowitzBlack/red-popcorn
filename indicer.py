
import csv
from fuzzywuzzy import fuzz


def load_movies():
    with open("data/tmdb_5000_movies.csv", 'r') as f:
        movieSet = csv.reader(f)
        for movie in movieSet:
            yield movie

def word_frequency(sentence):
    counter_dict = {}
    if sentence[-1] == '?' or sentence[-1] == '.' or sentence[-1] == ',':
        sentence = sentence[0:-1]
    for word in sentence.lower().split():
        if word not in counter_dict:
            counter_dict[word] = 0
        counter_dict[word] += 1
    return counter_dict

class MovieIndexer():

    def __init__(self,movieSet):
        self.movieSet = movieSet


    def split_for_clarity(self):
        #self.movieSet = movieSet
        for i,movie in enumerate(self.movieSet):
            # i is the index number for quick access
            # -2 is the avg rating
            # -1 is total votes
            # 6 is movie name
            title = movie[6]
            #word_freq = word_frequency(title)
            yield {"index_id":i,"movie_name":movie[6],"movie_rating":movie[-2],"movie_votes":movie[-1]}

    def find_movie(self,movieSet,search_movie_name):
        self.search_movie_name = search_movie_name
        self.movieSet = movieSet
        for mov in self.movieSet:
            #print(mov['movie_name'],fuzz.ratio(search_movie_name,mov['movie_name']))
            ratio = fuzz.ratio(search_movie_name,mov['movie_name'])
            if ratio > 55:
                yield mov["movie_name"]


if __name__ == "__main__":
    dataset = load_movies()
    x = MovieIndexer(dataset)
    split_data = list(x.split_for_clarity())
    found_movie_list = list(x.find_movie(split_data,"sex in the city"))
    for x in found_movie_list:
        print(x)
