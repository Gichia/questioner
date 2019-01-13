""" Contains all meetup DB Oprerations """
import datetime

posted_meetups = []
rsvps = []
meetup_id = 0


class MeetupsModel():
    """A class to include all meetups operations"""


    def get_all_meetups(self):
        """Method to get all meetups"""

        if len(posted_meetups) == 0:
            return False
        return posted_meetups


    def create_meetup(self, location, tags, topic, happening_on):
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
            posted_meetups.append(new_meetup)
            return new_meetup
        return {"status": "400", "message": "Please fill in all required fields"}


    def get_single_meetup(self, meetup_id):
        """Method to get a specific meetup"""
        if len(posted_meetups) == 0:
            return False
        for meetup in posted_meetups:
            if meetup["meetup_id"] == meetup_id:
                return meetup

    def meetup_rsvp(self, meetup_id, status):
        """Method to respond to meetup rsvp"""
        if len(posted_meetups) == 0:
            return False
        meetup = self.get_single_meetup(meetup_id)
        if meetup:
            new_rsvp = dict(
                meetup=meetup_id,
                status=status
            )
            rsvps.append(new_rsvp)
            return meetup_id
        return False
        