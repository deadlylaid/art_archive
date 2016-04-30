from flask import request

from sqlalchemy import or_

from api.artists.models import Artist
from api.artists.controllers import artists_api
from api.utils.json_decorator import json
from api.utils.response_wrapper import ok_response
from api.utils.errors import bad_request, unprocessable_entry
from api.utils.url_helper import get_absolute_url


@artists_api.route("/search/", methods=['GET'])
@json
def artists_search():

    params = {
        param: request.args[param]
        for param in request.args
        if param in ['name', 'country', 'genre', 'alive_in', 'max_items', 'order']
    }

    if not params:
        return bad_request("at least one parameter is required for search function")

    current_query = Artist.query
    if 'name' in params:
        current_query = Artist.query.filter(Artist.name.contains(params['name']))
    if 'country' in params:
        current_query = current_query.filter(Artist.country.contains(params['country']))
    if 'genre' in params:
        current_query = current_query.filter(Artist.genre.contains(params['genre']))
    if 'alive_in' in params:
        current_query = current_query.filter(Artist.birth_year <= params['alive_in']).\
                                        filter(or_(Artist.death_year == None, Artist.death_year >= params['alive_in']))
    if 'order' in params:
        order = params.get('order', 'asc')
        if order == "asc":
            current_query = current_query.order_by(Artist.created_at)
        elif order == "desc":
            current_query = current_query.order_by(-Artist.created_at)
        else:
            return unprocessable_entry("order parameter invalid, try desc or asc")

    max_items = params.get('max_items', None)
    if max_items:
        current_query = current_query.limit(max_items)

    query_result = current_query.all()

    data = []
    for artist in query_result:
        datum = artist.to_json
        datum['detail_href'] = \
            get_absolute_url('artists_api.artists_detail', artist_id=artist.id)
        data.append(datum)
    if not data:
        msg = "No results were retrieved from database"
        return ok_response(None, msg=msg)
    if max_items and int(max_items) > len(data):
        msg = "requested with max_items: \
            {0} but only {1} items were found \
            matching the query".format(max_items, len(data))
        return ok_response(data, msg=msg)
    return ok_response(data)
