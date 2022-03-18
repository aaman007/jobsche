from flask.views import MethodView
from flask_smorest import Blueprint


blp = Blueprint(
    'job',
    __name__,
    url_prefix='/api/job',
    description='Job related operations',
)
