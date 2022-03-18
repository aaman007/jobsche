class ObjectNotFound(Exception):
    def __init__(self, message):
        self.message = message or 'Object not found!'
        super().__init__()
