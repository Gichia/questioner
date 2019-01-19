"""Base model to initiate db operations"""
from app.db_conn import get_connection

class BaseModel:
    """Base model to initiate db"""
    def __init__(self):
        self.db = get_connection()

    def post_data(self, query, data):
        """Method to post data to db"""
        curr = self.db.cursor()
        curr.execute(query, data)
        self.db.commit()
        return data

    def get_email(self, email):
        """Method to check if email exist"""
        query = """SELECT email FROM users WHERE email=%s"""

        cursor = self.db.cursor()
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result
        