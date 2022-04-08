from modules.data.movieData import MovieList
from modules.data.userData import UserList
from modules.user import User


def register_user(movies: MovieList, users: UserList):
    #registering new user
    print("----***** Welcome to registration page *****----")
    name = input("Name : ")
    email = input("Email : ")
    phone = input("Phone : ")
    age = int(input("Age : "))
    password = input("Password : ")
    if email in users.userList:
        print("User is already present please return to  login page")
    else:
        users.add_user(User(name, email, phone, age, password))
        print("User is successfully registered")