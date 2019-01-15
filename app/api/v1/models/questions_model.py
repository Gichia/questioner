""" Contains all questions DB Oprerations """
from app.api.v1.models.basemodel import BaseModel
import datetime

posted_questions = []
question_id = 0
votes = 0


class QuestionsModel(BaseModel):
    """A class to include all question operations"""
    def __init__(self):
        self.questions = posted_questions
        self.votes = votes


    def get_single_question(self, question_id):
        """Method to get a single question"""
        if len(self.questions) == 0:
            return False
        for question in self.questions:
            if question["question_id"] == question_id:
                return question
            return False

    def get_question(self, question_id):
        """Method match if question exists"""
        question = self.get_single_question(question_id)
        if question:
            return question
        return False

    def post_question(self, meetup_id, title, body):
        """Method to post a new question to a specific meetup"""
        new_question = dict(
            question_id=len(self.questions) + 1,
            meetup = meetup_id,
            posted_on=datetime.datetime.now(),
            title=title,
            body=body,
            votes=votes
        )

        if new_question:
            self.questions.append(new_question)
            return new_question
        return False

    def get_meetup_questions(self, meetup_id):
        """Method to get all questions for a specific meetup"""
        if len(self.questions) == 0:
            return False
        for question in self.questions:
            questions = []
            if question["meetup"] == meetup_id:
                questions.append(question)
                return questions
            return False

    def upvote_question(self, question_id):
        """Method to upvote a question"""
        question = self.get_question(question_id)
        if question:
            question["votes"] += 1
            return question
        return False

    def downvote_question(self, question_id):
        """Method to upvote a question"""
        question = self.get_question(question_id)
        if question:
            question["votes"] -= 1
            return question
        return False
