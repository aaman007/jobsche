from uuid import uuid4

from jobsche.models.app import App
from jobsche.services.utils import BaseService


class AppService(BaseService):
    _model = App

    @classmethod
    def create(cls, data):
        app = App(
            name=data['name'],
            description=data['description'],
            secret_key=uuid4()
        )
        app.save()
        return app

    @classmethod
    def update(cls, guid, data):
        app = cls.find_by_guid(guid)
        app.name = data['name']
        app.description = data['description']
        app.save()
        return app

    @classmethod
    def delete(cls, guid):
        app = cls.find_by_guid(guid)
        app.delete()

    @classmethod
    def refresh_secret_key(cls, guid):
        app = cls.find_by_guid(guid)
        app.secret_key = uuid4()
        app.save()
        return app
