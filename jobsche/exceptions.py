class PublicException(Exception):
    pass


class PrivateException(Exception):
    pass


class ObjectNotFound(PublicException):
    def __init__(self, message=None):
        self.message = message or 'Object not found!'
        super().__init__()


class BadRequest(PublicException):
    pass


class Unauthorized(PublicException):
    pass


class Forbidden(PublicException):
    pass


class MethodNotAllowed(PublicException):
    pass


class ConfigurationError(PrivateException):
    pass
