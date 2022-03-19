class DemoMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Set X-Jobsche-Valid header
        environ['HTTP_X_JOBSCHE_VALID'] = 'Yes'

        # request does not exist at this point
        # from werkzeug.wrappers import Request
        # request = Request(environ, shallow=True)

        return self.app(environ, start_response)
