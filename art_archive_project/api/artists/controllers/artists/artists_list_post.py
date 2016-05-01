from flask import request

from api import db
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.nullify import nullify
from api.utils.errors import unprocessable_entry
from api.artists.utils import create_new_artist


@artists_api.route("/", methods=['POST'])
@json
def artists_list_post():
    input_params = ['name', 'country', 'genre', 'birth_year', 'death_year']
    params = {
        param: request.values[param]
        for param in request.values
        if param in input_params
        if nullify(request.values[param])
    }
    if not ('name' in params and 'country' in params and 'genre' in params):
        return unprocessable_entry("name, country, genre are required parameters")
    return create_new_artist(db, **params)
