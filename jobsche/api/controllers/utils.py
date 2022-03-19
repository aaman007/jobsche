from flask_smorest import abort

from jobsche.exceptions import (
    ObjectNotFound,
    BadRequest,
    Forbidden,
    PublicException,
)


def safe_service_call(service_method, *args, **kwargs):
    try:
        return service_method(*args, **kwargs)
    except BadRequest as e:
        abort(400, e.message)
    except Forbidden as e:
        abort(403, e.message)
    except ObjectNotFound as e:
        abort(404, message=e.message)
    except PublicException as e:
        abort(500, message=e.message)
    except Exception as _:
        abort(500, 'Something went wrong!')
