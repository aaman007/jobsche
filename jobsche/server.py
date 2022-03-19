from flask import Flask

from jobsche.api import create_api
from jobsche.admin import create_admin
from jobsche.models import *
from jobsche.config import Config
from jobsche.db import db


def create_app(config=None):
    flask_app = Flask(__name__)

    if config:
        flask_app.config.from_object(config)

    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()

    return flask_app


app = create_app(Config())
create_api(app)
create_admin(app)
