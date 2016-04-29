from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.errors import not_found


@artists_api.route("/<int:artist_id>/", methods=['GET'])
@json
def artists_detail(artist_id):
    artist = Artist.query.get(artist_id)
    if artist:
        data = artist.to_json
        data['artworks_href'] = \
            request.host_url[:-1] + url_for('artists_api.artists_artworks', artist_id=artist.id)
        return {"data": data}, 200
    return not_found("URL path invalid, check artist_id")
