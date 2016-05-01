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
        return ok_response(artist.to_json_with_artworks)
    return not_found("URL path invalid, check artist_id")
