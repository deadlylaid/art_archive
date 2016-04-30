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
    count = request.args.get('count', None)

    if order == 'asc':
        images = Image.query.order_by(Image.year).all()
    elif order == 'desc':
        images = Image.query.order_by(-Image.year).all()
    else:
        return unprocessable_entry("order parameter invalid, try desc or asc")

    if count:
        try:
            count = int(count)
            if count <= 0:
                return unprocessable_entry("count parameter must be 'positive' integer")
            images = images[:count]
        except ValueError:
            return unprocessable_entry("count parameter must be positive 'integer'")

    data = []
    for image in images:
        datum = image.to_json
        datum['detail_href'] = \
            get_absolute_url('images_api.images_detail', image_id=image.id)
        data.append(datum)
    return ok_response(data)
