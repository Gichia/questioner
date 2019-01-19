"""User class to store all db methods"""
import datetime
from werkzeug.security import generate_password_hash
from .basemodel import BaseModel


class UserClass(BaseModel):
    """Contains relevant db methods"""
        
    def save_user(self, firstname, lastname, email, password):
        """Method to add new user to db"""    
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "created_on": datetime.datetime.now(),
            "password": generate_password_hash(password)
        }

        query = """INSERT INTO users (firstname, lastname, email, created_on, password) VALUES
                    ( %(firstname)s, %(lastname)s, %(email)s, %(created_on)s, %(password)s )"""
        
        data = self.post_data(query, user)
        return data
