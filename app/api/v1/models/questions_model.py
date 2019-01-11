""" Contains all questions DB Oprerations """
import datetime

posted_questions = []
question_id = 0


class QuestionsModel():
    """A class to include all question operations"""

    def post_question(self, meetup_id, title, body):
        """Method to post a new question to a specific meetup"""
        new_question = dict(
            question_id=len(posted_questions) + 1,
            meetup = meetup_id,
            posted_on=datetime.datetime.now(),
            title=title,
            body=body
        )

        if new_question:
            posted_questions.append(new_question)
            return new_question
        return False
