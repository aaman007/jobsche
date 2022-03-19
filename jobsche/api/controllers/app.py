from flask.views import MethodView
from flask_smorest import Blueprint

from jobsche.api.controllers.utils import (
    safe_service_call,
    authorized_app
)
from jobsche.api.schemas.app import (
    AppSchema,
    SecretKeySchema
)
from jobsche.services.app import AppService


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
        return safe_service_call(AppService.find_by_guid, guid)

    @blp.arguments(AppSchema, location='json')
    @blp.response(200, AppSchema)
    @authorized_app()
    def put(self, data, guid):
        return safe_service_call(AppService.update, guid, data)

    @blp.response(204, None)
    @authorized_app()
    def delete(self, guid):
        safe_service_call(AppService.delete, guid)


@blp.route('/<string:guid>/secret-key')
class SecretKeyRetrieveView(MethodView):

    @blp.response(200, SecretKeySchema)
    def get(self, guid):
        return safe_service_call(AppService.find_by_guid, guid)


@blp.route('/<string:guid>/secret-key/refresh')
class SecretKeyRefreshView(MethodView):

    @blp.response(200, SecretKeySchema)
    @authorized_app()
    def post(self, guid):
        return safe_service_call(AppService.refresh_secret_key, guid)
