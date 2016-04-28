from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.errors import unprocessable_entry


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
            datum['detail_href'] = request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=artist.id)
            data.append(datum)
        return {"data": data}, 200

    if request.method == 'POST':
        from api import db

        name = request.values.get('name')
        country = request.values.get('country')
        genre = request.values.get('genre')

        from api.utils.nullify import nullify
        birth_year = nullify(request.values.get('birth_year'))
        death_year = nullify(request.values.get('death_year'))

        # Required Fields: name, country, genre
        if not (name and country and genre):
            return unprocessable_entry("name, country, genre are required parameters")

        new_artist = Artist(name=name, country=country, genre=genre, birth_year=birth_year, death_year=death_year)
        db.session.add(new_artist)

        try:
            db.session.commit()
            data = new_artist.to_json
            data['artworks_href'] = request.host_url[:-1] + url_for('artists_api.artists_artworks', artist_id=new_artist.id)
            return {"data": data}, 201

        except Exception:
            return unprocessable_entry("name, country, genre should be string, birth_year, death_year should by int")
