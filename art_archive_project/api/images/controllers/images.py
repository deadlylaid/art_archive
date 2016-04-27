from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json


@images_api.route("/", methods=['GET', 'POST'])
@json
def images_list():
    return {"test": "images_endpoint"}, 200
