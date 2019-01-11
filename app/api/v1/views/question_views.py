""" Create questions views' """
from flask import Flask, request, jsonify
from .. import ver1
from ... v1.models import questions_model
from ... v1.models import meetups_model


@ver1.route("/questions/<int:meetup_id>", methods=["POST"])
def post_question(meetup_id):
    """ Post question to specific meetup """
    # Get the requested meetup
    meetup = meetups_model.MeetupsModel().get_single_meetup(meetup_id)

    if meetup:
        data = request.get_json()
        if not data:
            return jsonify({
            'message': "Please fill in all fields!",
            'status': 401
            })
        new_question = questions_model.QuestionsModel().post_question(meetup_id, data["title"], data["body"])
        return jsonify({"status": 201, "message": "Successfully posted your question!", "data": new_question})
    return jsonify({"status": 404, "message": "That meetup does not exist!"})

@ver1.route("/questions/<int:meetup_id>", methods=["GET"])
def get_meetup_questions(meetup_id):
    """ Get questions for specific meetup """
    # Get the requested meetup
    meetup = meetups_model.MeetupsModel().get_single_meetup(meetup_id)

    if meetup:
        questions = questions_model.QuestionsModel().get_meetup_questions(meetup_id)
        if questions:
            return jsonify({"status": 200, "data": questions})
    return jsonify({"status": 404, "message": "That meetup does not exist!"})

@ver1.route("/questions/upvote/<int:question_id>", methods=["PATCH"])
def upvote_question(question_id):
    """ Upvote a question """
    # Get the requested question
    question = questions_model.QuestionsModel().get_single_question(question_id)

    if question:
        questions_model.QuestionsModel().upvote_question(question_id)
        return jsonify({"status": 404, "message": "Question successfully liked!"})
    return jsonify({"status": 404, "message": "That question does not exist!"})
