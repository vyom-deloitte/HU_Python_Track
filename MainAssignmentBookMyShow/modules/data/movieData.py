from modules.movie import Movie


class MovieList:
    def __init__(self):
        self.movieList = dict()

    def __str__(self):
        return str(list(self.movieList.keys()))

    def get_movie_list(self) -> list:
        return list(self.movieList.keys())

    def add_movie(self, movie: Movie):
        self.movieList[movie.movie_details['title']] = movie

    def del_movie(self, movie_name: str):
        try:
            self.movieList.pop(movie_name)
        except:
            print("Movie not found")
