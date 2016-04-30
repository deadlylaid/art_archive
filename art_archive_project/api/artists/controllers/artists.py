from flask import request

from api import db
from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response, created_response
from api.utils.errors import unprocessable_entry
from api.utils.url_helper import get_absolute_url
from api.utils.nullify import nullify


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
            datum['detail_href'] = get_absolute_url('artists_api.artists_detail', artist_id=artist.id)
            data.append(datum)
        return ok_response(data)

    if request.method == 'POST':

        input_params = ['name', 'country', 'genre', 'birth_year', 'death_year']

        params = {
            param: request.values[param]
            for param in request.values
            if param in input_params
            if nullify(request.values[param])
        }

        if not ('name' in params and 'country' in params and 'genre' in params):
            return unprocessable_entry("name, country, genre are required parameters")

        new_artist = Artist(**params)
        db.session.add(new_artist)

        try:
            db.session.commit()
            data = new_artist.to_json
            data['artworks_href'] = get_absolute_url('artists_api.artists_artworks', artist_id=new_artist.id)
            return created_response(data)

        except Exception:
            return unprocessable_entry("name, country, genre should be string, birth_year, death_year should by int")
