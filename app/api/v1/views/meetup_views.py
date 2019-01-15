""" Create meetuo views' """
from flask import Flask, request, jsonify, make_response
from .. import ver1
from ... v1.models import meetups_model


@ver1.route("/meetups", methods=["POST"])
def create_meetup():
    """ Post meetups """
    try:
        data = request.get_json()
        topic = data["topic"]
        location = data["location"]
        tags = data["tags"]
        happeningOn = data["happening_on"]
    except:
        return make_response(jsonify({
            "status": 500,
            "message": "Please provide correct details"
        }))

    new_meetup = meetups_model.MeetupsModel().create_meetup(location, tags, topic, happeningOn)
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


@ver1.route("meetups/upcoming", methods=["GET"])
def get_upcoming():
    """ Gets all upcoming meetups """
    meetups = meetups_model.posted_meetups

    if meetups:
        return jsonify({"status": 200, "data": meetups})
    return jsonify({"status": 404, "message": "No upcoming meetups"})


@ver1.route("/meetups/rsvp/<int:meetup_id>", methods=["POST"])
def meetup_rsvp(meetup_id):
    """ Respond to meetup rsvp """
    try:
        data = request.get_json()
        status = data["status"].lower()
    except:
        return make_response(jsonify({
            "status": 500,
            "message": "Please provide correct details"
        }))

    if (status != "yes" and status != "no" and status != "maybe"):
        return jsonify({"message": "Status can only be a yes, no or maybe"})
    meetup = meetups_model.MeetupsModel().get_single_meetup(meetup_id)
    if not meetup:
        jsonify({"status": 404, "message": "No meetup found"})
    meetup = meetups_model.MeetupsModel().meetup_rsvp(meetup_id, status)
    return jsonify({"status_code": 201, "status": status, "message": "Rsvp responded to!"})
 