""" Create meetuo views' """
from flask import Flask, request, jsonify
from .. import ver1
from ... v1.models import meetups_model


@ver1.route("/meetups", methods=["POST"])
def create_meetup():
    """ Post meetups """
    data = request.get_json()

    if not data:
        return jsonify({
            'message': "Please fill in all fields!",
            'status': 401
            })
    new_meetup = meetups_model.MeetupsModel().create_meetup(data['location'], data['tags'], data['topic'], data['happening_on'])
    return jsonify({"status": 201, "message": "New meetup created successfully!", "data": new_meetup})

@ver1.route("/meetups", methods=["GET"])
def get_all_meetups():
    """ Gets all meetups """
    meetups = meetups_model.posted_meetups

    if meetups:
        return jsonify({"status": 200, "data": meetups})
    return jsonify({"status": 404, "message": "No meetups found"})

@ver1.route("/meetups/<int:meetup_id>", methods=["GET"])
def get_single_meetup(meetup_id):
    """ Gets specific meetup """
    meetup = meetups_model.MeetupsModel().get_single_meetup(meetup_id)

    if meetup:
        return jsonify({"status": 200, "data": meetup})
    return jsonify({"status": 404, "message": "No meetup found!"})
