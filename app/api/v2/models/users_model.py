"""User class to store all db methods"""
from app.db_conn import get_connection


class UserClass():
    """User class to init user db"""
    def __init__(self):
        self.db = get_connection()

    def save_user(self, firstname, lastname, email, password, phone):
        """Method to add new user to db"""    
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "phonenumber": phone
        }

        query = """INSERT INTO users (firstname, lastname, email, password, phonenumber) VALUES
                    ( %(firstname)s, %(lastname)s, %(email)s, %(password)s, %(phonenumber)s )"""
        curr = self.db.cursor()
        curr.execute(query, user)
        self.db.commit()
