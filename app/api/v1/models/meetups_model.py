""" Contains all meetup DB Oprerations """
from app.api.v1.models.basemodel import BaseModel
import datetime

posted_meetups = []
posted_rsvps = []
meetup_id = 0


class MeetupsModel(BaseModel):
    """A class to include all meetups operations"""
    def __init__(self):
        self.meetups = posted_meetups
        self.rsvps = posted_rsvps

    def create_meetup(self, location, tags, topic, happening_on, *args):
        """Method to create a new meetup"""
        new_meetup = dict(
            meetup_id=len(posted_meetups) + 1,
            created_on=datetime.datetime.now(),
            location=location,
            topic=topic,
            happening_on=happening_on,
            tags=tags
        )

        if new_meetup:
            return self.post(posted_meetups, new_meetup)
        return {"status": "400", "message": "Please fill in all required fields"}
        
    def get_all_meetups(self):
        """Method to get all meetups"""
        return self.meetups

    def get_single_meetup(self, meetup_id):
        """Method to get a specific meetup"""
        if len(posted_meetups) == 0:
            return False
        for meetup in posted_meetups:
            if meetup["meetup_id"] == meetup_id:
                return meetup

    def get_meetup(self, question_id):
        """Method match if meetup exists"""
        meetup = self.get_single_meetup(meetup_id)
        if meetup:
            return meetup
        return False

    def meetup_rsvp(self, meetup_id, status):
        """Method to respond to meetup rsvp"""
        meetup = self.get_meetup(meetup_id)
        if meetup:
            new_rsvp = dict(
                meetup=meetup_id,
                status=status
            )
            self.rsvps.append(new_rsvp)
            return meetup_id
        return False
        