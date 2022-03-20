from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

from jobsche.api.controllers.utils import (
    safe_service_call,
    authorized_app
)
from jobsche.api.schemas.app import (
    AppSchema,
    AppQueryArgsSchema,
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


@blp.route('/item')
class RetrieveUpdateDestroyView(MethodView):

    @blp.arguments(AppQueryArgsSchema, location='query')
    @blp.response(200, AppSchema)
    def get(self, query):
        return safe_service_call(
            AppService.find_by_guid,
            query.get('guid')
        )

    @blp.arguments(AppSchema, location='json')
    @blp.response(200, AppSchema)
    @authorized_app()
    def put(self, data):
        return safe_service_call(
            AppService.update,
            request.app.guid,
            data
        )

    @blp.response(204, None)
    @authorized_app()
    def delete(self):
        safe_service_call(
            AppService.delete,
            request.app.guid
        )


@blp.route('/item/secret-key')
class SecretKeyRetrieveView(MethodView):

    @blp.arguments(AppQueryArgsSchema, location='query')
    @blp.response(200, SecretKeySchema)
    def get(self, query):
        return safe_service_call(
            AppService.find_by_guid,
            query.get('guid')
        )


@blp.route('/item/secret-key/refresh')
class SecretKeyRefreshView(MethodView):

    @blp.response(200, SecretKeySchema)
    @authorized_app()
    def post(self):
        return safe_service_call(
            AppService.refresh_secret_key,
            request.app.guid
        )
