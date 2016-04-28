from flask import url_for
from flask import request

from sqlalchemy import or_

from api.images.models import Image
from api.artists.models import Artist
from api.images.controllers import images_api
from api.utils.json_decorator import json


@images_api.route("/search/", methods=['GET'])
@json
def images_search():
    # Handling parameters
    title = request.args.get('title', None)
    year = request.args.get('year', None)

    # Get from artist
    artist_name = request.args.get('artist_name', None)
    genre = request.args.get('genre', None)
    description = request.args.get('description', None)

    max_items = request.args.get('max_items', None)
    order = request.args.get('order', None)

    if not (title or year or artist_name or genre or description or max_items or order):
        return {"error": "at least one parameter is required for search function"}, 400

    current_query = Image.query

    if title:
        current_query = current_query.filter(Image.title.contains(title))
    if year:
        current_query = current_query.filter(Image.year == year)
    if artist_name:
        current_query = current_query.join(Image.artist).filter(Artist.name.contains(artist_name))
    if genre:
        current_query = current_query.join(Image.artist).filter(Artist.genre.contains(genre))
    if order:
        if order == "asc":
            current_query = current_query.order_by(Image.year)
        elif order == "desc":
            current_query = current_query.order_by(-Image.year)
        else:
            return {"error": "order parameter invalid, try desc or asc"}, 422
    if max_items:
        current_query = current_query.limit(max_items)

    query_result = current_query.all()

    data = []
    for image in query_result:
        datum = image.to_json
        datum['genre'] = image.artist.genre
        datum['detail_href'] = request.host_url[:-1] + url_for('images_api.images_detail', image_id=image.id)
        data.append(datum)
    if not data:
        return {"meta": {"response_msg": "No results were retrieved from database"}, "data": None}, 200
    if max_items and int(max_items) > len(data):
        return {"meta": {"response_msg": "requested with max_items: \
                {0} but only {1} items were found matching the query"
                .format(max_items, len(data))}, "data": data}, 200
    return {"data": data}, 200
