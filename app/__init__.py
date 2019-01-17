from flask import Flask
from app.api.v1.utils.errors import bad_request, not_found, internal_server_error
from  app.api.v1.views.home import home
from .api.v1.views.user_views import ver1 as v1
from .api.v1.views.meetup_views import ver1 as v1
from .api.v1.views.question_views import ver1 as v1


def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(home)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(405, bad_request)
    app.register_error_handler(404, not_found)
    return app