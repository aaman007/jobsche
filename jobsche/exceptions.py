class ObjectNotFound(Exception):
    def __init__(self, message):
        self.message = 'Object not fouund!'
