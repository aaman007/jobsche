from uuid import uuid4

from jobsche.models.app import App
from jobsche.services.utils import BaseService


class AppService(BaseService):
    _model = App

    @classmethod
    def create(cls, data):
        app = App(**data, secret_key=uuid4())
        return app.save()

    @classmethod
    def refresh_secret_key(cls, guid):
        app = cls.find_by_guid(guid)
        app.secret_key = uuid4()
        app.save()
        return app
