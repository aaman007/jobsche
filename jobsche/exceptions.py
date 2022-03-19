class ObjectNotFound(Exception):
    def __init__(self, message):
        if not message:
            message = 'Object not found!'
        super().__init__(message)


class ConfigurationError(Exception):
    pass
