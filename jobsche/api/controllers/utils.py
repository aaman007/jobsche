from functools import wraps

from flask import request
from flask_smorest import abort

from jobsche.services.app import AppService
from jobsche.exceptions import (
    ObjectNotFound,
    BadRequest,
    Unauthorized,
    Forbidden,
    PublicException,
)


def safe_service_call(service_method, *args, **kwargs):
    try:
        return service_method(*args, **kwargs)
    except BadRequest as e:
        return abort(400, message=e.message)
    except Unauthorized as e:
        return abort(401, message=e.message)
    except Forbidden as e:
        return abort(403, message=e.message)
    except ObjectNotFound as e:
        return abort(404, message=e.message)
    except PublicException as e:
        return abort(500, message=e.message)
    except Exception as _:
        return abort(500, message='Something went wrong!')


def authorized_app():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            app_id = kwargs.get('guid')
            secret_key = request.headers.get('X-Secret-Key')

            if not secret_key:
                return abort(401, message='Missing X-Secret-Key header')

            request.app = safe_service_call(
                AppService.authenticate,
                app_id,
                secret_key,
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator
