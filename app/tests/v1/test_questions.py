"""File to test all questions endpoints"""
import json
from app.tests.v1.basetests import BaseTest


class TestMeetups(BaseTest):
    """ Class to test all questions endpoints """


    def test_post_question(self):
        """Test post question endpoint"""
        self.post(self.meetup_url, self.meetup)
        response = self.post(self.post_question, self.question)
        response2 = self.post(self.wrong_url, self.question)
        result = self.return_json(response)

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "Successfully posted your question!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response2.status_code, 404)
        self.assertEqual(response.content_type, "application/json")

    def test_meetup_questions(self):
        """Test get specific meetup questions"""
        self.post(self.meetup_url, self.meetup)
        self.post(self.post_question, self.question)
        response = self.get_items(self.meetup_questions)
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")


    def test_upvote_question(self):
        """Method to test upvote questions endpoint"""
        self.post(self.meetup_url, self.meetup)
        self.post(self.post_question, self.question)

        response = self.patch(self.upvote_question_url)
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question upvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")

    def test_downvote_question(self):
        """Method to test upvote question endpoint"""
        self.post(self.meetup_url, self.meetup)
        self.post(self.post_question, self.question)

        response = self.client.patch(self.downvote_question_url)
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(result["message"], "Question downvoted!")
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.content_type, "application/json")
