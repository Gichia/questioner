"""File to test all questions endpoints"""
import json
from app.tests.v1.basetests import BaseTest

wrong_url = "http://localhost:5000/api/v1/questions"
upvote_question_url = 'http://localhost:5000/api/v1/questions/upvote/1'
downvote_question_url = 'http://localhost:5000/api/v1/questions/downvote/1'

class TestMeetups(BaseTest):
    """ Class to test all questions endpoints """


    def test_post_question(self):
        """Test post question endpoint"""
        self.post_meetup()
        response = self.post_question()
        response2 = self.client.post(wrong_url, data=json.dumps(self.question), content_type="application/json")
        result = self.return_json(response)

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "Successfully posted your question!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response2.status_code, 404)
        self.assertEqual(response.content_type, "application/json")

    def test_meetup_questions(self):
        """Test get specific meetup questions"""
        self.post_meetup()
        self.post_question()
        response = self.meetup_questions()
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")


    def test_upvote_question(self):
        """Method to test upvote question endpoint"""
        self.post_meetup()
        self.post_question()

        response = self.client.patch(upvote_question_url, content_type="application/json")
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question upvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")

    def test_downvote_question(self):
        """Method to test upvote question endpoint"""
        self.post_meetup()
        self.post_question()

        response = self.client.patch(downvote_question_url, content_type="application/json")
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question downvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")
