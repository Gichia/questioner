""" Home view """
from flask import Flask, request, jsonify
from .. import home

@home.route('/')
def index():
    """Main function to return API endpoints"""
    response = {
       "get_all_metups" : "GET [api/v1/meetups]",
       "get_meetup_questions" : "GET [api/v1/questions/<meetup_id>]",
       "post_question" : "POST [api/v1/questions/<question_id>]",
       "upvote_question" : "PATCH [api/v1/questions/upvote/<question_id>]",
       "downvote_question" : "PATCH [api/v1/questions/downvote/<question_id>]",
       "respond_to_rsvp" : "POST [api/v1/meetups/rsvp/<meetup_id>]",
       "upcoming_meetups" : "GET [api/v1/meetups/upcoming]"
   }
    output = jsonify({"data" : response, "message" : "Try the following endpoints"})

    return output