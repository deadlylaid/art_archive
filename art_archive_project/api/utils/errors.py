from api.utils.json_decorator import json


def unprocessable_entry(message):
    return {"error": message}, 422


def not_found(message):
    return {"error": message}, 404


def bad_request(message):
    return {"error": message}, 400


def internal_server_error():
    return {"error": "The server encountered an unexpected condition \
        which prevented it from fulfilling the request."}, 500
