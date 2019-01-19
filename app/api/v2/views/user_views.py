"""User endpoints"""
from flask import request, jsonify, make_response
from app.api.v2.models.users_model import UserClass
from app.api.v2 import ver2

db = UserClass()

@ver2.route("/auth/signup", methods=["POST"])
def user_signup():
    """Register new user endpoint"""
    try:
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        password = data["password"]
    except:
        return make_response(jsonify({
            "status": 500,
            "message": "Please provide correct details"
        }))

    # Validations
    phone = data["phone"]
    db.save_user(firstname, lastname, email, password, phone)
    return 'True'
