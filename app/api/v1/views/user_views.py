"""Contains all user endpoints"""
from werkzeug.security import generate_password_hash
from flask import Flask, request, jsonify, make_response
from .. import ver1
from ... v1.models import users_model
from .. utils.validations import Validations


validate = Validations()


@ver1.route("/auth/signup", methods=["POST"])
def register_user():
    """ Registers a new user"""

    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "Please fill in all fields!"})
    elif validate.is_valid_email(data["email"]) == False:
        return jsonify({"message": "Not a valid email"})
    elif validate.is_valid_password(data["password"]) == False:
        return jsonify({"message": "Not a valid password"})
    elif users_model.UserModel().username_exist(data["username"]) == True:
        return jsonify({"message": "Username exists!"})
    elif users_model.UserModel().email_exist(data["email"]) == True:
        return jsonify({"message": "Email exists!"})
    else:
        password = generate_password_hash(data['password'], method='sha256')
        new_user = users_model.UserModel().register_user(data["firstname"], data["lastname"], data["email"], data["phone_number"], data["username"], password)
        return jsonify({"status": 201, "message": "You have been successfully registered!", "data": new_user})


@ver1.route("/auth/login")
def login_user():
    """ Login a user"""

    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Please provide login info!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    token = users_model.UserModel().login_user(auth.username, auth.password)
    if not token:
        return jsonify({"status": 401, "message": "Incorrect login details!"})
    user = users_model.UserModel().authenticate_token(token)
    user_data = dict(
        id=user["user_id"],
        username=user["username"],
        email=user["email"],
        firstname=user["firstname"],
        lastname=user["lastname"]
    )
    return jsonify({"status": 200, "message": "Welcome to questioner, you have been successfully logged in!", "user": user_data})
       