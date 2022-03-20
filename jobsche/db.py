from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def initialize_db(flask_app):
    db.init_app(flask_app)
    Migrate(flask_app, db)
    return db
