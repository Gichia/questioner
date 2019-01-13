"""File to test all questions endpoints"""
import unittest
import json
from app import create_app


APP = create_app('testing')

post_meetup_url = 'http://localhost:5000/api/v1/meetups'
post_question_url = 'http://localhost:5000/api/v1/questions/1'
upvote_question_url = 'http://localhost:5000/api/v1/questions/upvote/1'
downvote_question_url = 'http://localhost:5000/api/v1/questions/downvote/1'

class TestMeetups(unittest.TestCase):
    """ Class to test all questions endpoints """

    def setUp(self):
        """Setup to store values to be used in the tests"""
        APP.testing = True
        self.app = APP.test_client()
        self.test_data = {
            "location": "Nairobi", 
            "topic": "Intro to JS",
            "happening_on": "11/2/2019",
            "tags": ["Beginners", "JS"]
            }
        self.test_data2 = {"title": "Question One", "body": "Suggested question One"}

    def test_post_question(self):
        """Test poste question endpoint"""
        self.app.post(post_meetup_url, data=json.dumps(self.test_data), content_type="application/json")
        response = self.app.post(post_question_url, data=json.dumps(self.test_data2), content_type="application/json")
        response2 = self.app.post("http://localhost:5000/api/v1/questions", data=json.dumps(self.test_data2), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "Successfully posted your question!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response2.status_code, 404)
        self.assertEqual(response.content_type, "application/json")

    def test_upvote_question(self):
        """Method to test upvote question endpoint"""
        self.app.post(post_meetup_url, data=json.dumps(self.test_data), content_type="application/json")
        self.app.post(post_question_url, data=json.dumps(self.test_data2), content_type="application/json")

        response = self.app.patch(upvote_question_url, content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question upvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")

    def test_downvote_question(self):
        """Method to test upvote question endpoint"""
        self.app.post(post_meetup_url, data=json.dumps(self.test_data), content_type="application/json")
        self.app.post(post_question_url, data=json.dumps(self.test_data2), content_type="application/json")

        response = self.app.patch(downvote_question_url, content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question downvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")


if __name__ == '__main__':
    unittest.main()
