"""Contains all user endpoints"""
from flask import Flask, request, jsonify, make_response
from .. import ver1
from ... v1.models import users_model
from werkzeug.security import generate_password_hash
from functools import wraps


@ver1.route("/auth/signup", methods=["POST"])
def register_user():
    """ Registers a new user"""

    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "Please fill in all fields!"})
    password = generate_password_hash(data['password'], method='sha256')
    new_user = users_model.UserModel().register_user(data["firstname"], data["lastname"], data["email"], data["phone_number"], data["username"], password)
    return jsonify({"status": 201, "message": "You have been successfully registered!", "data": new_user})


@ver1.route("/auth/login")
def login_user():
    """ Login a user"""
