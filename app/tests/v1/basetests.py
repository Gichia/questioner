"""This includes the base class for our tests"""
import unittest
import json
from app import create_app


class BaseTest(unittest.TestCase):
    """Initializes our setUp for tests"""

    def setUp(self):
        """Initializes our app and tests"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.meetup_url = 'http://localhost:5000/api/v1/meetups'
        self.upcoming = 'http://localhost:5000/api/v1/meetups/upcoming'
        self.rsvp_url = 'http://localhost:5000/api/v1/meetups/rsvp/1'
        self.post_question = 'http://localhost:5000/api/v1/questions/1'
        self.specific_meetup = 'http://localhost:5000/api/v1/meetups/1'
        self.meetup_questions = 'http://localhost:5000/api/v1/questions/1'
        self.wrong_url = "http://localhost:5000/api/v1/questions"
        self.upvote_question_url = 'http://localhost:5000/api/v1/questions/upvote/1'
        self.downvote_question_url = 'http://localhost:5000/api/v1/questions/downvote/1'
        self.meetup = {
            "location": "Nairobi", 
            "topic": "Intro to JS", 
            "happening_on": "11/2/2019", 
            "tags": ["Beginners", "JS"]
        }
        self.question = {
            "title": "Question One", 
            "body": "Suggested question One"
        }
        self.rsvp = {
            "status": "maybe"
        }

    def post(self, url, db):
        return self.client.post(url, data=json.dumps(db), content_type="application/json")

    def get_items(self, url):
        return self.client.get(url)

    def patch(self, url):
        return self.client.patch(url, content_type="application/json")

    def return_json(self, response):
        """Return json formated response for test purpose"""
        return json.loads(response.data.decode("UTF-8"))


    def tearDown(self):
        """Tear down the app after running tests"""
        self.app = None


    if __name__ == '__main__':
        unittest.main()