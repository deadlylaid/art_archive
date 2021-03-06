from flask import request

from api import db
from api.images.models import Image
from api.artists.models import Artist
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import unprocessable_entry
from api.utils.response_wrapper import ok_response, created_response
from api.utils.url_helper import get_absolute_url
from api.utils.nullify import nullify


@images_api.route("/", methods=['GET'])
@json
def images_list_get():
    order = request.args.get('order', 'asc')
    count = request.args.get('count', None, type=int)

    images_query, error = Image.filter_by_order(Image.query, order)
    if error: return error

    images = images_query.all()

    if count:
        images = images[:count]

    data = [image.to_json_with_detail for image in images]
    return ok_response(data)
