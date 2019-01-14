"""This includes the base class for our tests"""
import unittest
import json
from app import create_app

meetup_url = 'http://localhost:5000/api/v1/meetups'
upcoming = 'http://localhost:5000/api/v1/meetups/upcoming'
rsvp_url = 'http://localhost:5000/api/v1/meetups/rsvp/1'
post_question = 'http://localhost:5000/api/v1/questions/1'
specific_meetup = 'http://localhost:5000/api/v1/meetups/1'
meetup_questions = 'http://localhost:5000/api/v1/questions/1'


class BaseTest(unittest.TestCase):
    """Initializes our setUp for tests"""

    def setUp(self):
        """Initializes our app and tests"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
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


    def post_meetup(self):
        """Create a valid post for test purposes"""
        return self.client.post(meetup_url, data=json.dumps(self.meetup), content_type="application/json")

    def get_meetups(self):
        """Get all meetup"""
        return self.client.get(meetup_url)

    def get_upcoming(self):
        """Get upcoming meetups"""
        return self.client.get(upcoming)

    def post_rsvp(self):
        """Post rsvp for testing"""
        return self.client.post(rsvp_url, data=json.dumps(self.rsvp), content_type="application/json")
    
    def get_single_meetup(self):
        """Get specific meetup"""
        return self.client.get(specific_meetup)

    def post_question(self):
        """Post a question for test purposes"""
        return self.client.post(post_question, data=json.dumps(self.question), content_type="application/json")

    def meetup_questions(self):
        """Get specific meetup questions for test purposes"""
        return self.client.get(meetup_questions)

    def return_json(self, response):
        """Return json formated response for test purpose"""
        return json.loads(response.data.decode("UTF-8"))


    def tearDown(self):
        """Tear down the app after running tests"""
        self.app = None


    if __name__ == '__main__':
        unittest.main()