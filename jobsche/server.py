from flask import Flask

from jobsche.api import create_api
from jobsche.admin import create_admin
from jobsche.models import *
from jobsche.middlewares.demo import DemoMiddleware
from jobsche.config import Config
from jobsche.db import db


def register_middlewares(app):
    app.wsgi_app = DemoMiddleware(app.wsgi_app)
    return app


def create_app(config=None):
    flask_app = Flask(__name__)

    if config:
        flask_app.config.from_object(config)

    register_middlewares(flask_app)

    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()

    return flask_app


app = create_app(Config())
create_api(app)
create_admin(app)
