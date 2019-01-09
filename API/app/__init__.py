from flask import Flask
from .api.v1.views.user_views import ver1 as v1


def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app