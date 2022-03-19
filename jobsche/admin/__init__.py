from flask import Blueprint

from jobsche.admin.home import blp as home_blp


def register_blueprints(blp):
    blp.register_blueprint(home_blp)


def create_admin(app):
    blp = Blueprint(
        'admin',
        __name__,
        url_prefix='/admin'
    )

    register_blueprints(blp)
    app.register_blueprint(blp)

    return blp
