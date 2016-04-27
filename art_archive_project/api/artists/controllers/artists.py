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
        pass
