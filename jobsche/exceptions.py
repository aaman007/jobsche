from mailbox import Message


class ObjectNotFound(Exception):
    def __init__(self, message):
        self.message = message or 'Object not found!'
        super().__init__()


class ConfigurationError(Exception):
    pass
