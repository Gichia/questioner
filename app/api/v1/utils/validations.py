"""Class to include validations"""
import re
import datetime

class Validations:
    """Validation methods"""
    def is_valid_email(self, email):
        """Validate email"""
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is None:
            return False
        return True

    def is_valid_password(self, password):
        """Validate password"""
        if len(password) < 6 and len(password) > 12:
            return False
        if re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@&])[A-Za-z0-9$#@&]{6,}", password) is None:
            return False
        return True

    def is_only_string(self, phrase):
        """Validate only string"""
        for item in phrase:
            if type(item) != str:
                return False
        return True
            
    def is_future_date(self, date):
        """VAlidate future date"""
        if date > datetime.date.today():
            return True
        else:
            return False