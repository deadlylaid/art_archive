from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json


@artists_api.route("/<int:artist_id>/artworks/", methods=['GET'])
@json
def artists_artworks(artist_id):
    artist = Artist.query.get(artist_id)
    if artist:
        data = []
        for image in artist.images:
            datum = image.to_json
            datum['detail_href'] = \
                request.host_url[:-1] + url_for('images_api.images_detail', image_id=image.id)
            data.append(datum)
        return {"data": data}, 200
    return {"error": "URL path invalid, check artist_id"}, 404
