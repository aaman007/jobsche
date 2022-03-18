from flask_smorest import Api

from jobsche.api.controllers.app import blp as app_blp
from jobsche.api.controllers.job import blp as job_blp


def create_api(app):
    api = Api(app)

    api.register_blueprint(app_blp)
    api.register_blueprint(job_blp)

    return api
