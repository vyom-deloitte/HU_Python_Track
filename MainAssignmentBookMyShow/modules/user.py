from modules.movie import Movie


class User:
    def __init__(self, name, email, phone, age, password):
        #Constructor
        self.details = {'name': name, 'email': email, 'phone': phone, 'age': age, 'password': password}
        self.bookings = dict()#this dictionary keeps tracks of all the tickets of current user


    def show_booking_details(self):
        #shows timing and tickets of the currently booked movie
        for k, v in self.bookings.items():
            print(f"{k} => {v}")

    def show_all_bookings(self) -> list:
        #shows all movies that are booked as of now
        res = list(self.bookings.keys())
        for i in range(len(res)):
            print(f"{i+1}. {res[i]}")
        return res

    def give_user_rating(self, rating: int, movie: Movie):
        #to give user rating
        rating = max(1, rating)
        rating = min(10, rating)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print("You haven't watch the movie yet")
            return
        movie.add_user_rating(rating)
        print("User rating added")

    def book_show(self, movie: Movie, timing: str, seats: int):
        #to book a show
        if movie.time_slot[timing] >= seats:#if available seats are more than the seats that we are trying to book
            movie.time_slot[timing] -= seats
            title = movie.movie_details['title']
            if title in self.bookings:
                if timing in self.bookings[title]: self.bookings[title][timing] += seats
                else: self.bookings[title][timing] = seats
            else: self.bookings[title] = {timing: seats}
        else:
            print("The number of seats you are trying to book are not available")

    def cancel_show(self, movie: Movie, timing: str, seats: int):
        #to cancel tickets
        print(self.bookings)
        title = movie.movie_details['title']
        if title not in self.bookings:
            print(f"No booking of {title} movie")
            return
        if timing not in self.bookings[title]:
            print(f"You have no booking of {title} at {timing} slot")
            return

        if seats > self.bookings[title][timing]:
            print("You are trying to cancel more seats than you have booked")
        else:
            self.bookings[title][timing] -= seats #reducing booked number of seats
            movie.time_slot[timing] += seats #increasing empty seats
            # if all seats are cancelled
            if self.bookings[title][timing] == 0: self.bookings[title].pop(timing) #remove title from bookings dictionary
            if len(self.bookings[title]) == 0: self.bookings.pop(title)#remove timing from bookings dictionary
            print("Cancellation successful")

    def show_timings(self, title: str):
        #shows all timings for a movie
        res = list(self.bookings[title].keys())
        for i in range(len(res)):
            print(f"{i + 1}. {res[i]}")
        return res