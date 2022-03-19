class PublicException(Exception):
    pass


class PrivateException(Exception):
    pass


class ObjectNotFound(PublicException):
    def __init__(self, message=None):
        self.message = message or 'Object not found!'
        super().__init__()


class BadRequest(PublicException):
    def __init__(self, message=None):
        self.message = message or 'BadRequest!'
        super().__init__()


class Unauthorized(PublicException):
    def __init__(self, message=None):
        self.message = message or 'Unauthorized!'
        super().__init__()


class Forbidden(PublicException):
    def __init__(self, message=None):
        self.message = message or 'Forbidden!'
        super().__init__()


class MethodNotAllowed(PublicException):
    def __init__(self, message=None):
        self.message = message or 'MethodNotAllowed!'
        super().__init__()


class ConfigurationError(PrivateException):
    def __init__(self, message=None):
        self.message = message or 'ConfigurationError!'
        super().__init__()
