from flask import request

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import not_found
from api.utils.response_wrapper import ok_response


@images_api.route("/<int:image_id>/", methods=['GET'])
@json
def images_detail(image_id):
    image = Image.query.get(image_id)
    if image:
        return ok_response(image.to_json_with_artist)
    return not_found("URL path invalid, check image_id")
