from modules.data.movieData import MovieList
from modules.movie import Movie


def getMins(s: str, foundHr: bool) -> int:
    s = s.split()
    hr, mins = 0, 0
    for i in s:
        if '0' <= i[0] <= '9':
            if not foundHr: hr, foundHr = int(i), True
            else: mins = int(i)
    return hr*60+mins


class Admin:
    def __init__(self):
        #Setting admin fields in the constructor
        self.username = "MovieMafia"
        self.password = "abcdef"

    def login(self, username, password) -> bool:
        #This login function validates login credentials of Admin
        return self.username == username and self.password == password

    def get_movie(self) -> Movie:
        #taking input for movie details
        title = input("Enter movie title :")
        genre = input("Provide Movie Genre : ")
        rating = input("Enter Admin Rating : ")
        language = input("Enter Language of the movie: ")
        showCnt = int(input("Enter No of shows in a day : "))
        length = getMins(input("Enter Length in hours :"), False)
        cast = input("Enter the movie Cast :")
        director = input("Movie Director Name : ")
        cap = int(input("Hall Capacity : "))
        fs = getMins(input("First Show : "), False)
        interval = getMins(input("Enter interval timing in minutes: "), True)
        gap = getMins(input("Enter gap time between two shows in minutes : "), True)

        return Movie(title, genre, length, cast, director, rating, language, showCnt, fs, interval,gap, cap)

    def add_movie(self, movies: MovieList):
        #adding movie to MovieList
        print("-----***** Admin Add Movie *****-----")
        movieObject = self.get_movie()
        title = movieObject.movie_details['title'] #checking whether the movie we are adding already exists
        if title not in movies.movieList.keys(): movies.add_movie(movieObject)
        else: print("Movie is already listed")

    def edit_movie(self, movies: MovieList):
        #Editing already existing move
        #All fields except title can be edited
        print("----***** Admin Edit Movie *****-----")
        movieObject = self.get_movie()
        if movieObject.movie_details['title'] in movies.movieList.keys():
            movies.movieList[movieObject.movie_details['title']] = movieObject
            print("Update is successful")

        else:
            print("Update Unsuccessful, no movie of this title is found")

    def delete_movie(self, movies: MovieList):
        #Deleting already existing move
        print("***** Admin Delete Movie *****")
        lst = list(movies.movieList.keys())
        for i in range(len(lst)):
            print(f"{i+1}. {lst[i]}")
        inp = int(input("Enter which movie you want to delete : ")) - 1
        movies.movieList.pop(lst[inp])

    def logout(self):
        print("Admin is successfully logged out")
