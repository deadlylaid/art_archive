from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response
from api.utils.errors import unprocessable_entry
from api.utils.url_helper import get_absolute_url
from api.utils.nullify import nullify


@artists_api.route("/", methods=['GET'])
@json
def artists_list_get():
    order = request.args.get('order', 'asc')
    count = request.args.get('count', None, type=int)

    artists_query, error = Artist.filter_by_order(Artist.query, order)
    if error: return error

    artists = artists_query.all()

    if count:
        artists = artists[:count]

    data = [artist.to_json_with_detail for artist in artists]
    return ok_response(data)
