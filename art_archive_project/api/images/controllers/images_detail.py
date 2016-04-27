from flask import url_for
from flask import request

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json


@images_api.route("/<int:image_id>/", methods=['GET'])
@json
def images_detail(image_id):
    image = Image.query.get(image_id)
    if image:
        data = {}
        data['id'] = image.id
        data['image_url'] = image.image_url
        data['title'] = image.title
        data['year'] = image.year
        data['artist_id'] = image.artist.id
        data['artist_name'] = image.artist.name
        data['description'] = image.description
        data['artist_href'] = \
            request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=image.artist.id)
        return {"data": data}, 200
    return {"error": "URL path invalid, check image_id"}, 404
