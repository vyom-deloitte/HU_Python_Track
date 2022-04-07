from modules.data.movieData import MovieList
from modules.data.userData import UserList
from modules.user import User


def register_user(movies: MovieList, users: UserList):
    print("***** Welcome to registration page *****")
    name = input("Name = ")
    email = input("Email = ")
    phone = input("Phone = ")
    age = int(input("Age = "))
    password = input("Password = ")
    if email in users.ulist:
        print("User Already present go to the login page")
    else:
        users.add_user(User(name, email, phone, age, password))
        print("User successfully registered")