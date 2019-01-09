from flask import Flask, request, jsonify
from .. import ver1


@ver1.route("/", methods=["GET"])
def hello():
    """ Returns 'hello world' """

    return 'Home'