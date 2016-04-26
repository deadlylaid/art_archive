from flask import Blueprint
from flask import jsonify

from api import app


test_api = Blueprint('test', __name__, url_prefix='/test')


@test_api.route("/api/")
def get_api():
    test_response = {"Hello": "World", "Welcome": "to our API"}
    return jsonify(test_response)
