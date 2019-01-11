"""File to test all questions endpoints"""
import unittest
import json
from app import create_app


APP = create_app('testing')

post_meetup_url = 'http://localhost:5000/api/v1/meetups'
post_question_url = 'http://localhost:5000/api/v1/questions/1'
upvote_question_url = 'http://localhost:5000/api/v1/questions/upvote/1'

class TestMeetups(unittest.TestCase):
    """ Class to test all questions endpoints """

    def setUp(self):
        """Setup to store values to be used in the tests"""
        APP.testing = True
        self.app = APP.test_client()


    def test_upvote_question(self):
        """Method to test upvote question endpoint"""
        test_data = {"location": "Nairobi", "topic": "Intro to JS", "happening_on": "11/2/2019", "tags": ["Beginners", "JS"]}
        test_data2 = {"title": "Question One", "body": "Suggested question One"}
        self.app.post(post_meetup_url, data=json.dumps(test_data), content_type="application/json")
        self.app.post(post_question_url, data=json.dumps(test_data2), content_type="application/json")

        response = self.app.patch(upvote_question_url, content_type="application/json")
        result = result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question successfully liked!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")


if __name__ == '__main__':
    unittest.main()
