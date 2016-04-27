from flask import request

from api.images.models import Image
from api.images.controllers import images_api
from api.utils.json_decorator import json


@images_api.route("/", methods=['GET', 'POST'])
@json
def images_list():
    if request.method == 'GET':

        # Handling parameters
        order = request.args.get('order', 'asc')
        count = request.args.get('count', None)

        if order == 'asc':
            images = Image.query.order_by(Image.id).all()
        elif order == 'desc':
            images = Image.query.order_by(-Image.id).all()
        else:
            return {"error": "order parameter invalid, try desc or asc"}, 422

        if count:
            try:
                count = int(count)
                if count <= 0:
                    return {"error": "count parameter must be 'positive' integer"}, 422
                images = images[:count]
            except ValueError:
                return {"error": "count parameter must be positive 'integer'"}, 422

        data = []
        for image in images:
            datum = {}
            datum['id'] = image.id
            datum['image_url'] = image.image_url
            datum['title'] = image.title
            datum['year'] = image.year
            datum['artist_id'] = image.artist_id
            datum['artist_name'] = image.artist.name
            datum['description'] = image.description
            datum['detail_href'] = request.host_url[:-1]  # + url_for('artists_api.artists_detail', artist_id=artist.id)
            data.append(datum)
        return {"data": data}, 200
