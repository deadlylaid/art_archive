from flask import request

from sqlalchemy import or_

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response
from api.utils.errors import bad_request


@artists_api.route("/search/", methods=['GET'])
@json
def artists_search():
    params = {
        param: request.args[param]
        for param in request.args
        if param in ['name', 'country', 'genre', 'alive_in', 'max_items', 'order']
    }
    if not params:
        return bad_request("at least one parameter is required for search function")

    query_result, error = Artist.filter_by_params(params)
    if error: return error

    data = [artist.to_json_with_detail for artist in query_result]
    return ok_response(data, **params)
