"""Contains all user DB operations"""
import datetime
import jwt
from werkzeug.security import check_password_hash
from instance.config import Config

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

    def login_user(self, username, password):
        """Functtion to login in user"""
        for user in users:
            if user["username"] == username:
                user_password = user["password"]
                if check_password_hash(user_password, password):
                    token = jwt.encode({'sub': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)
                    return token
            return False

    def authenticate_token(self, token):
        """Authenticate user token"""
        if not token:
            return False
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = UserModel().get_single_user(data["sub"])
        except:
            return False
        return current_user["user_id"]

    def username_exist(self, username):
        """Check if username exists"""
        for user in users:
            if user["username"] == username:
                return True
            return False

    def email_exist(self, email):
        """Check if email exists"""
        for user in users:
            if user["email"] == email:
                return True
            return False
        