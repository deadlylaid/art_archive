from flask import jsonify
from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api


@artists_api.route("/<int:artist_id>/")
def artists_detail(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    data = {}
    data['id'] = artist.id
    data['name'] = artist.name
    data['birth_year'] = artist.birth_year
    data['death_year'] = artist.death_year
    data['country'] = artist.country
    data['genre'] = artist.genre
    data['artworks_href'] = "Not implemented yet"
    artists_response = {"meta": {"response_code": 200}, "data": data}
    return jsonify(artists_response)
