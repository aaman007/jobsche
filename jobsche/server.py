from flask import Flask

from jobsche.api import create_api
from jobsche.admin import create_admin
from jobsche.models import *
from jobsche.middlewares.demo import DemoMiddleware
from jobsche.config import Config
from jobsche.db import initialize_db


def register_middlewares(flask_app):
    flask_app.wsgi_app = DemoMiddleware(flask_app.wsgi_app)
    return flask_app


def create_app(config=None):
    flask_app = Flask(__name__)

    if config:
        flask_app.config.from_object(config)

    register_middlewares(flask_app)
    initialize_db(flask_app)

    return flask_app


app = create_app(Config())
create_api(app)
create_admin(app)
