from modules.user import User


class UserList:
    def __init__(self):
        self.userList = dict()

    def __str__(self):
        return str(set(self.userList.keys()))

    def add_user(self, user: User):
        self.userList[user.details['email']] = user

    def delete_user(self, name:str):
        try:
            self.userList.pop(name)
        except:
            print("user not found, deletion unsuccessful")