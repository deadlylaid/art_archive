from flask import request

from sqlalchemy import or_

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import bad_request
from api.utils.response_wrapper import ok_response
from api.utils.url_helper import get_absolute_url


@images_api.route("/search/", methods=['GET'])
@json
def images_search():
    params = {
        param: request.args[param]
        for param in request.args
        if param in ['title', 'year', 'artist_name', 'description', 'genre', 'max_items', 'order']
    }
    if not params:
        return bad_request("at least one parameter is required for search function")

    query_result, error = Image.filter_by_params(params)
    if error: return error

    data = [image.to_json_search_result for image in query_result]
    return ok_response(data, **params)
