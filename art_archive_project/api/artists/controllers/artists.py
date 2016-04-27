from flask import jsonify
from flask import url_for
from flask import request

from api.artists.models import Artist
from api.artists.controllers import artists_api


@artists_api.route("/", methods=['GET', 'POST'])
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
            return jsonify(
                    {
                        "meta": {
                            "response_code": 422,
                            "error_type": "UNPROCESSABLE ENTRY",
                            "error_msg": "order parameter invalid, try desc or asc",
                        },
                        "data": None
                    }
            )

        if count:
            try:
                count = int(count)
                if count <= 0:
                    return jsonify(
                        {
                            "meta": {
                                "response_code": 422,
                                "error_type": "UNPROCESSABLE ENTRY",
                                "error_msg": "count parameter must be 'positive' integer",
                            },
                            "data": None
                        }
                    )
                artists = artists[:count]
            except ValueError:
                return jsonify(
                        {
                            "meta": {
                                "response_code": 422,
                                "error_type": "UNPROCESSABLE ENTRY",
                                "error_msg": "count parameter must be positive 'integer'",
                            },
                            "data": None
                        }
                )
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
        artists_response = {"meta": {"response_code": 200}, "data": data}
        return jsonify(artists_response)

    if request.method == 'POST':
        from api import db

        name = request.values.get('name')
        country = request.values.get('country')
        genre = request.values.get('genre')
        birth_year = request.values.get('birth_year')
        death_year = request.values.get('death_year')

        # Required Fields: name, country, genre
        if not (name and country and genre):
            return jsonify(
                    {
                        "meta": {
                            "response_code": 422,
                            "error_type": "UNPROCESSABLE ENTRY",
                            "error_msg": "name, country, genre are required parameters",
                        },
                        "data": None
                    }
            )

        new_artist = Artist(name=name, country=country, genre=genre, birth_year=birth_year, death_year=death_year)
        db.session.add(new_artist)

        from _mysql_exceptions import OperationalError
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

            return jsonify(
                {
                    "meta": {
                        "response_code": 200,
                    },
                    "data": data
                }
            )
        except OperationalError:
            return jsonify(
                {
                    "meta": {
                        "response_code": 422,
                        "error_type": "UNPROCESSABLE ENTRY",
                        "error_msg": "name, country, genre should be string, birth_year, death_year should by int",
                    },
                    "data": None
                }
            )
