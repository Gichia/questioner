"""File to test all meetup endpoints"""
from app.tests.v1.basetests import BaseTest


specific_meetups = 'http://localhost:5000/api/v1/meetups/1'


class TestMeetups(BaseTest):
    """ Class to test all meetup endpoints """

    def test_post_meetup(self):
        """Method to test get all meetups endpoint"""
        response = self.post_meetup()
        result = self.return_json(response)

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "New meetup created successfully!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_get_all_meetups(self):
        """A test for the get all meetups endpoint"""
        self.post_meetup()
        response = self.get_meetups()
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_get_specific_meetup(self):
        """Method to test get specific meetup endpoint"""
        self.post_meetup()
        results = self.get_single_meetup()
        result1 = self.return_json(results)

        self.assertEqual(result1["status"], 200)
        self.assertEqual(results.status_code, 200)
        self.assertEqual(results.status, "200 OK")
        self.assertTrue(results.content_type == "application/json")
    
    def test_get_upcoming(self):
        """Test for get upcoming meetups endpoint"""
        self.post_meetup()
        response = self.get_upcoming()
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_rsvp(self):
        """Test respond to meetup rsvp"""
        self.post_meetup()
        response = self.post_rsvp()
        result = self.return_json(response)

        self.assertIn("Rsvp responded to!", result["message"])
        self.assertEqual(result["status_code"], 201)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")



