from flask.views import MethodView
from flask_smorest import Blueprint, abort

from jobsche.api.schemas.app import AppSchema
from jobsche.services.app import AppService
from jobsche.exceptions import ObjectNotFound


blp = Blueprint(
    'app',
    __name__,
    url_prefix='/api/app',
    description='App related operations',
)


@blp.route('')
class ListCreateView(MethodView):

    @blp.response(200, AppSchema(many=True))
    def get(self):
        return AppService.find_all()

    @blp.arguments(AppSchema, location='json')
    @blp.response(201, AppSchema)
    def post(self, data):
        return AppService.create(data)


@blp.route('/<string:guid>')
class RetrieveUpdateDestroyView(MethodView):

    @blp.response(200, AppSchema)
    def get(self, guid):
        try:
            return AppService.find_by_guid(guid)
        except ObjectNotFound as e:
            abort(404, message=e.message)
        except Exception as e:
            abort(500, 'Something went wrong!')

    @blp.arguments(AppSchema, location='json')
    @blp.response(200, AppSchema)
    def put(self, data, guid):
        try:
            return AppService.update(guid, data)
        except ObjectNotFound as e:
            abort(404, message=e.message)
        except Exception as e:
            abort(500, 'Something went wrong!')

    @blp.response(204, None)
    def delete(self, guid):
        try:
            return AppService.delete(guid)
        except ObjectNotFound as e:
            abort(404, message=e.message)
        except Exception as e:
            abort(500, 'Something went wrong!')
