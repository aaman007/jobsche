class ObjectNotFound(Exception):
    def __init__(self, message=None):
        self.message = message or 'Object not found!'
        super().__init__()


class ConfigurationError(Exception):
    pass
