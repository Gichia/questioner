"""File to test all meetup endpoints"""
from app.tests.v1.basetests import BaseTest


class TestMeetups(BaseTest):
    """ Class to test all meetup endpoints """

    def test_post_meetup(self):
        """Method to test get all meetups endpoint"""
        response = self.post(self.meetup_url, self.meetup)
        result = self.return_json(response)

        self.assertEqual(result["status"], 201)
        self.assertEqual(result["message"], "New meetup created successfully!")
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_get_all_meetups(self):
        """A test for the get all meetups endpoint"""
        self.post(self.meetup_url, self.meetup)
        response = self.get_items(self.meetup_url)
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_get_specific_meetup(self):
        """Method to test get specific meetup endpoint"""
        self.post(self.meetup_url, self.meetup)
        results = self.get_items(self.meetup_url)
        result1 = self.return_json(results)

        self.assertEqual(result1["status"], 200)
        self.assertEqual(results.status_code, 200)
        self.assertEqual(results.status, "200 OK")
        self.assertTrue(results.content_type == "application/json")
    
    def test_get_upcoming(self):
        """Test for get upcoming meetups endpoint"""
        self.post(self.meetup_url, self.meetup)
        response = self.get_items(self.upcoming)
        result = self.return_json(response)

        self.assertEqual(result["status"], 200)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")

    def test_rsvp(self):
        """Test respond to meetup rsvp"""
        self.post(self.meetup_url, self.meetup)
        response = self.post(self.rsvp_url, self.rsvp)
        result = self.return_json(response)

        self.assertIn("Rsvp responded to!", result["message"])
        self.assertEqual(result["status_code"], 201)
        self.assertEqual(response.status, "200 OK")
        self.assertTrue(response.content_type == "application/json")



