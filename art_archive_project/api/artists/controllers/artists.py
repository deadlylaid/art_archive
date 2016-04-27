from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json


@artists_api.route("/", methods=['GET', 'POST'])
@json
def artists_list():
    if request.method == 'GET':

        # Handling parameters
        order = request.args.get('order', 'asc')
        count = request.args.get('count', None)

        if order == 'asc':
            artists = Artist.query.order_by(Artist.id).all()
        elif order == 'desc':
            artists = Artist.query.order_by(-Artist.id).all()
        else:
            return {"error": "order parameter invalid, try desc or asc"}, 422

        if count:
            try:
                count = int(count)
                if count <= 0:
                    return {"error": "count parameter must be 'positive' integer"}, 422
                artists = artists[:count]
            except ValueError:
                return {"error": "count parameter must be positive 'integer'"}, 422

        data = []
        for artist in artists:
            datum = {}
            datum['id'] = artist.id
            datum['name'] = artist.name
            datum['birth_year'] = artist.birth_year
            datum['death_year'] = artist.death_year
            datum['country'] = artist.country
            datum['genre'] = artist.genre
            datum['detail_href'] = request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=artist.id)
            data.append(datum)
        return {"data": data}, 200

    if request.method == 'POST':
        from api import db

        name = request.values.get('name')
        country = request.values.get('country')
        genre = request.values.get('genre')
        birth_year = request.values.get('birth_year')
        death_year = request.values.get('death_year')

        # Required Fields: name, country, genre
        if not (name and country and genre):
            return {"error": "name, country, genre are required parameters"}, 422

        new_artist = Artist(name=name, country=country, genre=genre, birth_year=birth_year, death_year=death_year)
        db.session.add(new_artist)

        try:
            db.session.commit()
            data = {}
            data['id'] = new_artist.id
            data['name'] = new_artist.name
            data['birth_year'] = new_artist.birth_year
            data['death_year'] = new_artist.death_year
            data['country'] = new_artist.country
            data['genre'] = new_artist.genre
            data['artworks_href'] = "Not implemented yet"
            return {"data": data}, 200

        except Exception:
            return {"error": "name, country, genre should be string, birth_year, death_year should by int"}, 422
