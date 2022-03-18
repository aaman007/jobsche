from jobsche.models.app import App
from jobsche.exceptions import ObjectNotFound


class AppService:

    @classmethod
    def find_all(cls):
        return App.query.all()

    @classmethod
    def find_by_guid(cls, guid):
        app = App.query.filter_by(guid=guid).first()
        if not app:
            raise ObjectNotFound(f'App with guid {guid} not found')
        return app

    @classmethod
    def create(cls, data):
        app = App(
            name=data['name'],
            description=data['description'],
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
