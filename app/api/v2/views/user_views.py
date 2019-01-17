"""User endpoints"""
from flask import request, jsonify
from app.api.v2 import ver2


@ver2.route('/auth/signup')
def user_signup():
    """Register new user endpoint"""
    return 'Home'
