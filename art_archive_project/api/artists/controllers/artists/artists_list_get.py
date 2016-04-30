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

    if order == 'asc':
        artists = Artist.query.order_by(Artist.id).all()
    elif order == 'desc':
        artists = Artist.query.order_by(-Artist.id).all()
    else:
        return unprocessable_entry("order parameter invalid, try desc or asc")
    if count:
        artists = artists[:count]

    data = [artist.to_json_with_detail for artist in artists]
    return ok_response(data)
