""" Contains all meetup DB Oprerations """
import datetime

posted_meetups = []
meetup_id = []


class MeetupsModel():
    """A cless to include all meetups operations"""


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
