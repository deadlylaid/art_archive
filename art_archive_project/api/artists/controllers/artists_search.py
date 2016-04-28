from flask import url_for
from flask import request

from sqlalchemy import or_

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json


@artists_api.route("/search/", methods=['GET'])
@json
def artists_search():
    # Handling parameters
    name = request.args.get('name', None)
    country = request.args.get('country', None)
    genre = request.args.get('genre', None)
    alive_in = request.args.get('alive_in', None)
    max_items = request.args.get('max_items', None)
    order = request.args.get('order', None)

    if not (name or country or genre or alive_in or max_items or order):
        return {"error": "at least one parameter is required for search function"}, 400

    current_query = Artist.query

    if name:
        current_query = Artist.query.filter(Artist.name.contains(name))
    if country:
        current_query = current_query.filter(Artist.country.contains(country))
    if genre:
        current_query = current_query.filter(Artist.genre.contains(genre))
    if alive_in:
        current_query = current_query.filter(Artist.birth_year <= alive_in).\
                                        filter(or_(Artist.death_year == None, Artist.death_year >= alive_in))
    if order:
        if order == "asc":
            current_query = current_query.order_by(Artist.created_at)
        elif order == "desc":
            current_query = current_query.order_by(-Artist.created_at)
        else:
            return {"error": "order parameter invalid, try desc or asc"}, 422
    if max_items:
        current_query = current_query.limit(max_items)

    query_result = current_query.all()

    data = []
    for artist in query_result:
        datum = artist.to_json
        datum['detail_href'] = \
            request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=artist.id)
        data.append(datum)
    if not data:
        return {"meta": {"response_msg": "No results were retrieved from database"}, "data": None}, 200
    if max_items and int(max_items) > len(data):
        return {"meta": {"response_msg": "requested with max_items: \
                {0} but only {1} items were found matching the query"
                .format(max_items, len(data))}, "data": data}, 200
    return {"data": data}, 200
