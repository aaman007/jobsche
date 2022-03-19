from uuid import uuid4

from jobsche.models.app import App
from jobsche.services.utils import BaseService
from jobsche.exceptions import Unauthorized


class AppService(BaseService):
    _model = App

    @classmethod
    def refresh_secret_key(cls, guid):
        app = cls.find_by_guid(guid)
        app.secret_key = uuid4()
        return app.save()

    @classmethod
    def authenticate(cls, guid, secret_key):
        app = cls.find_by_guid(guid)
        if app.secret_key != secret_key:
            raise Unauthorized('Secret key is invalid.')
        return app
