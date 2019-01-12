"""Contains all user DB operations"""
import datetime

users = []
user_id = 0

class UserModel():
    """A class to include all user operations"""

    def register_user(self, firstname, lastname, email, phone_number, username, password):
        """A method to register a new user"""

        new_user = dict(
            user_id=len(users) + 1,
            firstname=firstname,
            lastname=lastname,
            registered=datetime.datetime.now(),
            email=email,
            phone_number=phone_number,
            username=username,
            password=password,
            isAdmin=False
        )

        if new_user:
            users.append(new_user)
            return new_user
        return False

    def get_single_user(self, username):
        """A method to get a single user by username"""

        if len(users) == 0:
            return False
        for user in users:
            if user["username"] == username:
                return user
