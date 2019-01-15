"""A class to include all the base db functions"""

class BaseModel():
    """Base model to include all db methods"""

    def post(self, db, data):
        """Method to post data to db"""
        db.append(data)
        return data
