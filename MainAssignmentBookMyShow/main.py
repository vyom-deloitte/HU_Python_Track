from modules.data.movieData import MovieList
from modules.data.userData import UserList
from modules.login import login
from modules.register import register_user

movies = MovieList()
users = UserList()
while True:
    print("******Welcome to BookMyShow*******")
    print("1. Login")
    print("2. Register new Account")
    print("3. exit")

    inp = input()
    if inp == '1':
        #login user
        login(movies, users) #login user method call
        for i in movies.mlist.values():
            print(i)

    elif inp == '2':
        # register user
        register_user(movies, users)  # register user method call
        for i in movies.mlist.values():
            print(i)





    else: exit(0)