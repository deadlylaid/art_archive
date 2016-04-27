import functools
from flask import jsonify


def json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        data, response_code = f(*args, **kwargs)
        api_response = jsonify(data)
        api_response.status_code = response_code
        return api_response
    return wrapped
