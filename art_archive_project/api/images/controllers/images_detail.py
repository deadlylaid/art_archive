from flask import url_for
from flask import request

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import not_found


@images_api.route("/<int:image_id>/", methods=['GET'])
@json
def images_detail(image_id):
    image = Image.query.get(image_id)
    if image:
        data = image.to_json
        data['artist_href'] = \
            request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=image.artist.id)
        return {"data": data}, 200
    return not_found("URL path invalid, check image_id")
