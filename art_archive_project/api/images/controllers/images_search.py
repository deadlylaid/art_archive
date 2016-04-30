from flask import request

from sqlalchemy import or_

from api.images.models import Image
from api.artists.models import Artist
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import bad_request, unprocessable_entry
from api.utils.response_wrapper import ok_response
from api.utils.url_helper import get_absolute_url


@images_api.route("/search/", methods=['GET'])
@json
def images_search():
    title = request.args.get('title', None)
    year = request.args.get('year', None)

    artist_name = request.args.get('artist_name', None)
    genre = request.args.get('genre', None)
    description = request.args.get('description', None)

    max_items = request.args.get('max_items', None)
    order = request.args.get('order', None)

    if not (title or year or artist_name or genre or description or max_items or order):
        return bad_request("at least one parameter is required for search function")

    current_query = Image.query

    if title:
        current_query = current_query.filter(Image.title.contains(title))
    if year:
        current_query = current_query.filter(Image.year == year)
    if artist_name:
        current_query = current_query.join(Image.artist).filter(Artist.name.contains(artist_name))
    if genre:
        current_query = current_query.join(Image.artist).filter(Artist.genre.contains(genre))
    if description:
        current_query = current_query.filter(Image.description.contains(description))
    if order:
        if order == "asc":
            current_query = current_query.order_by(Image.year)
        elif order == "desc":
            current_query = current_query.order_by(-Image.year)
        else:
            return unprocessable_entry("order parameter invalid, try desc or asc")
    if max_items:
        current_query = current_query.limit(max_items)

    query_result = current_query.all()

    data = []
    for image in query_result:
        datum = image.to_json
        datum['genre'] = image.artist.genre
        datum['detail_href'] = get_absolute_url('images_api.images_detail', image_id=image.id)
        data.append(datum)
    if not data:
        msg = "No results were retrieved from database"
        return ok_response(None, msg=msg)
        
    if max_items and int(max_items) > len(data):
        msg = "requested with max_items: \
                {0} but only {1} item were found \
                matching the query".format(max_items, len(data))
        return ok_response(data, msg=msg)
    return ok_response(data)
