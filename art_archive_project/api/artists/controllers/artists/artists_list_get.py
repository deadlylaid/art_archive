from flask import request

from api import db
from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response, created_response
from api.utils.errors import unprocessable_entry
from api.utils.url_helper import get_absolute_url
from api.utils.nullify import nullify

@artists_api.route("/", methods=['GET'])
@json
def artists_list_get():
    order = request.args.get('order', 'asc')
    count = request.args.get('count', None)

    if order == 'asc':
        artists = Artist.query.order_by(Artist.id).all()
    elif order == 'desc':
        artists = Artist.query.order_by(-Artist.id).all()
    else:
        return unprocessable_entry("order parameter invalid, try desc or asc")

    if count:
        try:
            count = int(count)
            if count <= 0:
                return unprocessable_entry("count parameter must be 'positive' integer")
            artists = artists[:count]
        except ValueError:
            return unprocessable_entry("count parameter must be positive 'integer'")

    data = []
    for artist in artists:
        datum = artist.to_json
        datum['detail_href'] = get_absolute_url('artists_api.artists_detail', artist_id=artist.id)
        data.append(datum)
    return ok_response(data)
