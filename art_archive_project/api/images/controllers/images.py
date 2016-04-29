from flask import request
from flask import url_for

from api.images.models import Image
from api.artists.models import Artist
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import unprocessable_entry


@images_api.route("/", methods=['GET', 'POST'])
@json
def images_list():
    if request.method == 'GET':

        # Handling parameters
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
                request.host_url[:-1] + url_for('images_api.images_detail', image_id=image.id)
            data.append(datum)
        return {"data": data}, 200

    if request.method == 'POST':
        from api import db
        from api.utils.nullify import nullify

        required_params = ['title', 'image_url', 'image_year', 'artist_name', 'image_description']

        params = {
            param: request.values[param]
            for param in request.values
            if param in required_params
            if nullify(request.values[param])
        }

        if len(params) != len(required_params):
            return unprocessable_entry("title, image_url, image_year, artist_name, image_description are required parameters")

        artist = Artist.query.filter(Artist.name == params['artist_name']).first()
        if not artist:
            return unprocessable_entry("artist_name not found, artist_name should be in our artists database to add new image.")

        new_image = Image(
            artist=artist,
            **params
        )

        db.session.add(new_image)

        try:
            db.session.commit()
            data = new_image.to_json
            data['detail_href'] = \
                request.host_url[:-1] + url_for('images_api.images_detail', image_id=new_image.id)
            return {"data": data}, 201

        except Exception:
            return unprocessable_entry("title, image_url, description should be string, year should be integer")
