from flask import Flask, request, jsonify
from .. import ver1


@ver1.route("/meetups", methods=["GET"])
def get_all_meetups():
    """ Returns 'hello world' """

    return 'All meetups posted here...'