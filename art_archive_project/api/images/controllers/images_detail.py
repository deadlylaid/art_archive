from flask import request

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import not_found
from api.utils.response_wrapper import ok_response
from api.utils.url_helper import get_absolute_url


@images_api.route("/<int:image_id>/", methods=['GET'])
@json
def images_detail(image_id):
    image = Image.query.get(image_id)
    if image:
        data = image.to_json
        data['artist_href'] = get_absolute_url('artists_api.artists_detail', artist_id=image.artist.id)
        return ok_response(data)
    return not_found("URL path invalid, check image_id")
