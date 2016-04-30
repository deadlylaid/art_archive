from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response
from api.utils.errors import not_found
from api.utils.url_helper import get_absolute_url


@artists_api.route("/<int:artist_id>/", methods=['GET'])
@json
def artists_detail(artist_id):
    artist = Artist.query.get(artist_id)
    if artist:
        data = artist.to_json
        data['artworks_href'] = \
            get_absolute_url('artists_api.artists_artworks', artist_id=artist.id)
        return ok_response(data)
    return not_found("URL path invalid, check artist_id")
