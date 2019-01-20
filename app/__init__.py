from flask import Flask
from .api.v1.views.user_views import ver1 as v1
from .api.v1.views.meetup_views import ver1 as v1
from .api.v1.views.question_views import ver1 as v1
from .api.v2.views.user_views import ver2 as v2
from .api.v2.views.meetup_views import ver2 as v2


def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    return app