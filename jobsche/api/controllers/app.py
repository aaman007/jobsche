from flask.views import MethodView
from flask_smorest import Blueprint, abort

from jobsche.api.schemas.app import (
    AppResponseSchema,
    SecretKeyResponseSchema
)
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
        try:
            return AppService.find_by_guid(guid)
        except ObjectNotFound as e:
            return abort(404, message=e.message)
        except Exception as _:
            return abort(500, 'Something went wrong!')

    @blp.arguments(AppResponseSchema, location='json')
    @blp.response(200, AppResponseSchema)
    def put(self, data, guid):
        try:
            return AppService.update(guid, data)
        except ObjectNotFound as e:
            return abort(404, message=e.message)
        except Exception as _:
            return abort(500, 'Something went wrong!')

    @blp.response(204, None)
    def delete(self, guid):
        try:
            return AppService.delete(guid)
        except ObjectNotFound as e:
            return abort(404, message=e.message)
        except Exception as _:
            return abort(500, 'Something went wrong!')


@blp.route('/<string:guid>/secret-key')
class SecretKeyRetrieveView(MethodView):

    @blp.response(200, SecretKeyResponseSchema)
    def get(self, guid):
        try:
            return AppService.find_by_guid(guid)
        except ObjectNotFound as e:
            return abort(404, message=e.message)
        except Exception as _:
            return abort(500, 'Something went wrong!')


@blp.route('/<string:guid>/secret-key/refresh')
class SecretKeyRefreshView(MethodView):

    @blp.response(200, SecretKeyResponseSchema)
    def post(self, guid):
        try:
            return AppService.refresh_secret_key(guid)
        except ObjectNotFound as e:
            return abort(404, message=e.message)
        except Exception as _:
            return abort(500, 'Something went wrong!')
