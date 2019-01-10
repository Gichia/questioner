"""File to test all meetup endpoints"""
import unittest
import json
from app import create_app
from app.api.v1.models.meetups_model import MeetupsModel

APP = create_app('testing')

get_all_meetups_url = 'http://localhost:5000/api/v1/meetups'
get_specific_meetup_url = 'http://localhost:5000/api/v1/meetups/1'

class TestMeetups(unittest.TestCase):
    """ Class to test all meetup endpoints """

    def setUp(self):
        """Setup to store values to be used in the tests"""
        APP.testing = True
        self.app = APP.test_client()


    def test_get_all_meetups(self):
        """Method to test get all meetups endpoint"""
        test_data = {"location": "Nairobi", "topic": "Intro to JS", "happening_on": "11/2/2019", "tags": ["Beginners", "JS"]}
        response = self.app.post(get_all_meetups_url, data=json.dumps(test_data), content_type="application/json")
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "New meetup created successfully!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_get_specific_meetup(self):
        test_data = {"location": "Nairobi", "topic": "Intro to JS", "happening_on": "11/2/2019", "tags": ["Beginners", "JS"]}
        self.app.post(get_all_meetups_url, data=json.dumps(test_data), content_type="application/json")
        result = self.app.get(get_specific_meetup_url)

        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
