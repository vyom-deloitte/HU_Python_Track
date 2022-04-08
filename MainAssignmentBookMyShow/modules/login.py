from modules.admin import Admin
from modules.data.movieData import MovieList
from modules.data.userData import UserList

def login(movies: MovieList, users: UserList):
    while True:
        # Login Menu
        print("----***** Welcome to BookMyShow Login ******----")
        print("Enter 1. for Admin Login")
        print("Enter 2. for User Login")
        print("Enter 3. to go back to previous menu")

        inp = input()
        if inp == '1':
            admin_login(movies)
        elif inp == '2':
            user_login(movies, users)
        else:
            break

def user_login(movies: MovieList, users: UserList):#User Login
    print("----**** Welcome to User Login page****----")
    email = input("Email = ")
    password = input("Password = ")
    if email not in users.userList.keys():
        print("No user present with this email address. Kindly go to the registration page")
        return
    if users.userList[email].details['password'] != password:
        print("Wrong password")
        return

    print("Login successful")
    user = users.userList[email]

    print(f"Welcome {user.details['name']}")
    while True:
        lst = movies.get_movie_list()
        if len(lst) == 0:
            print("No movie has been registered yet")
            return
        for i in range(len(lst)):
            print(f"{i+1}. {lst[i]}")
        inp = int(input("Enter the number corresponds to the movie = ")) - 1
        if inp >= len(lst) or inp < 0:
            print("Not a proper movie index")
            continue
        movieObject = movies.movieList[lst[inp]]
        print(movieObject)

        print("1. Book ticket")
        print("2. Cancel ticket")
        print("3. Give user rating")
        print("4. exit")
        inp = int(input())
        if inp == 1:
            print("choose timing")
            slots = movieObject.get_timings()
            for i in range(len(slots)):
                print(f"{i+1}. {slots[i][0]} has {slots[i][1]} seats")
            inp = int(input()) - 1
            user.book_show(movieObject, slots[inp][0], int(input("No of Seats = ")))
        elif inp == 2:
            print("choose timing")
            slots = movieObject.get_timings()
            for i in range(len(slots)):
                print(f"{i + 1}. {slots[i][0]} has {slots[i][1]} seats")
            inp = int(input()) - 1
            user.cancel_show(movieObject, slots[inp][0], int(input("NO of seats = ")))

        elif inp == 3:
            user.give_user_rating(int(input("Give a rating between 1 to 10 = ")), movieObject)
            print("Avg movie rating = ", movieObject.get_user_rating())

        else: break

def admin_login(movies: MovieList):#Admin Login
    admin = Admin() #creating Admin object
    try:
        if not admin.login(input("Username = "), input("Password = ")):
            raise Exception("Admin details incorrect") # checking whether correct admin details are entered or not
    except Exception as e:
        print(e)
        return
    while True:
        #Admin Menu
        print("******Welcome Admin*******") #after successful login of admin this menu shows up
        print("1. Add new Movie")
        print("2. Edit movie")
        print("3. Delete Movie")
        print("4. Logout")
        ip = input()
        if ip == '1':
            admin.add_movie(movies) # calling add movie
        elif ip == '2':
            admin.edit_movie(movies) # calling edit movie
        elif ip == '3':
            admin.delete_movie(movies) # calling delete movie
        else:
            admin.logout() # calling logut
            return






