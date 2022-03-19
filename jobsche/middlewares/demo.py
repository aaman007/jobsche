class DemoMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # Set X-Jobsche-Valid header
        environ['HTTP_X_JOBSCHE_VALID'] = 'Yes'

        # request does not exist at this point
        # from werkzeug.wrappers import Request
        # request = Request(environ, shallow=True)

        return self.wsgi_app(environ, start_response)
