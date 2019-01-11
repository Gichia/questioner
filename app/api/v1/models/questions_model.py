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
            body=body,
            votes=0
        )

        if new_question:
            posted_questions.append(new_question)
            return new_question
        return False

    def get_meetup_questions(self, meetup_id):
        """Method to get all questions for a specific meetup"""
        if len(posted_questions) == 0:
            return False
        for question in posted_questions:
            questions = []
            if question["meetup"] == meetup_id:
                questions.append(question)
                return questions
            return False

    def get_single_question(self, question_id):
        """Method to get a single question"""
        if len(posted_questions) == 0:
            return False
        for question in posted_questions:
            if question["question_id"] == question_id:
                return question
            return False

    def upvote_question(self, question_id):
        """Method to upvote a question"""
        if len(posted_questions) == 0:
            return False
        for question in posted_questions:
            if question["question_id"] == question_id:
                question["votes"] += 1
            return False 
