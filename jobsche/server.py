from flask import Flask, jsonify

from jobsche.api import create_api
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


@app.route('/hello', methods=['GET'])
def home():
    return 'Hello World!'


@app.route('/', methods=['GET'])
def data():
    return jsonify([{'data': 'Hello World'}])
