from jobsche.exceptions import ObjectNotFound, ConfigurationError


class BaseService:
    _model = None

    @classmethod
    def _check_model_or_raise(cls):
        if not cls._model:
            raise ConfigurationError('No model class specified')

    @classmethod
    def find_all(cls):
        cls._check_model_or_raise()
        return cls._model.query.all()

    @classmethod
    def find_by_guid(cls, guid):
        cls._check_model_or_raise()
        obj = cls._model.query.filter_by(guid=guid).first()
        if not obj:
            raise ObjectNotFound(f'Object with guid {guid} not found')
        return obj
