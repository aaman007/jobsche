from flask.views import MethodView
from flask_smorest import Blueprint

from jobsche.api.controllers.utils import safe_service_call
from jobsche.api.schemas.app import (
    AppResponseSchema,
    SecretKeyResponseSchema
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

    @blp.response(200, AppResponseSchema(many=True))
    def get(self):
        return AppService.find_all()

    @blp.arguments(AppResponseSchema, location='json')
    @blp.response(201, AppResponseSchema)
    def post(self, data):
        return AppService.create(data)


@blp.route('/<string:guid>')
class RetrieveUpdateDestroyView(MethodView):

    @blp.response(200, AppResponseSchema)
    def get(self, guid):
        return safe_service_call(AppService.find_by_guid, guid)

    @blp.arguments(AppResponseSchema, location='json')
    @blp.response(200, AppResponseSchema)
    def put(self, data, guid):
        return safe_service_call(AppService.update, guid, data)

    @blp.response(204, None)
    def delete(self, guid):
        safe_service_call(AppService.delete, guid)


@blp.route('/<string:guid>/secret-key')
class SecretKeyRetrieveView(MethodView):

    @blp.response(200, SecretKeyResponseSchema)
    def get(self, guid):
        return safe_service_call(AppService.find_by_guid, guid)


@blp.route('/<string:guid>/secret-key/refresh')
class SecretKeyRefreshView(MethodView):

    @blp.response(200, SecretKeyResponseSchema)
    def post(self, guid):
        return safe_service_call(AppService.refresh_secret_key, guid)
