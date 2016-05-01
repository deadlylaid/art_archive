from flask import jsonify

from api import app


def unprocessable_entry(message):
    return {"error": message}, 422


def not_found(message):
    return {"error": message}, 404


def bad_request(message):
    return {"error": message}, 400


@app.errorhandler(500)
def internal_server_error(error):
    error_msg = jsonify({"error": "The server encountered an unexpected condition \
        which prevented it from fulfilling the request."})
    error_msg.status_code = 500
    return error_msg
