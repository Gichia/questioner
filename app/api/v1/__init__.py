from flask import Blueprint

ver1 = Blueprint("ver1", __name__, url_prefix="/api/v1")
home = Blueprint("home", __name__, url_prefix="/")