from flask import Blueprint
from flask import jsonify
from flask import render_template

test_api = Blueprint('test', __name__, url_prefix='/')


@test_api.route("/")
def get_api():
    return render_template('client.html')
