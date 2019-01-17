""" Create questions views' """
from flask import Flask, request, jsonify, make_response
from .. import ver1
from ... v1.models import questions_model
from ... v1.models import meetups_model


@ver1.route("/questions/<int:meetup_id>", methods=["POST"])
def post_question(meetup_id):
    """ Post question to specific meetup """
    try:
        data = request.get_json()
        title = data["title"]
        body = data["body"]
    except:
        return make_response(jsonify({
            "status": 500,
            "message": "Make sure sure fields are accurate!"
        }))
    
    if not title.strip():
        return jsonify({"message": "Please add a title!"})
    elif not body.strip():
        return jsonify({"message": "Please add a body!"})

    # Get the requested meetup
    meetup = meetups_model.MeetupsModel().get_single_meetup(meetup_id)

    if meetup:
        new_question = questions_model.QuestionsModel().post_question(meetup_id, title, body)
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
        return jsonify({"status": 404, "message": "No questions posted, be the first!"})
    return jsonify({"status": 404, "message": "That meetup does not exist!"})

@ver1.route("/questions/upvote/<int:question_id>", methods=["PATCH"])
def upvote_question(question_id):
    """ Upvote a question """
    # Get the requested question
    question = questions_model.QuestionsModel().upvote_question(question_id)

    if question:
        return jsonify({"status": 200, "message": "Question upvoted!", "data": question})
    return jsonify({"status": 404, "message": "Question not found!"}, 404)

@ver1.route("/questions/downvote/<int:question_id>", methods=["PATCH"])
def downvote_question(question_id):
    """ Upvote a question """
    # Get the requested question
    question = questions_model.QuestionsModel().downvote_question(question_id)

    if question:
        return jsonify({"status": 200, "message": "Question downvoted!", "data": question})
    return jsonify({"status": 404, "message": "Question not found!"}, 404)
