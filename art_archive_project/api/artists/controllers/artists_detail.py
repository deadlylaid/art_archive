from flask import jsonify
from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json


@artists_api.route("/<int:artist_id>/")
@json
def artists_detail(artist_id):
    artist = Artist.query.get(artist_id)
    if artist:
        data = {}
        data['id'] = artist.id
        data['name'] = artist.name
        data['birth_year'] = artist.birth_year
        data['death_year'] = artist.death_year
        data['country'] = artist.country
        data['genre'] = artist.genre
        data['artworks_href'] = "Not implemented yet"
        return {"data": data}, 200
    return {"error": "URL path invalid, check artist_id"}, 404
