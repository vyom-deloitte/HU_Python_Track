from modules.data.movieData import MovieList
from modules.data.userData import UserList
from modules.login import login
from modules.register import register_user

movies = MovieList() #creating MovieList object
users = UserList()  #creating UserList object
while True:
    print("----****Welcome to BookMyShow****----")
    print("Press 1. to Login")
    print("Press 2. to Register new Account")
    print("Press 3.to exit")

    inp = input()
    if inp == '1':
        #login user
        login(movies, users) #login user method call
        for i in movies.movieList.values():
            print(i)#printing all current movies

    elif inp == '2':
        # register user
        register_user(movies, users)  # register user method call
        for i in users.userList.values():
            print(i) #printing all current users

    else: exit(0)