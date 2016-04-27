from flask import request
from flask import url_for

from api.images.models import Image
from api.artists.models import Artist
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
            datum['artist_href'] = \
                request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=image.artist.id)
            data.append(datum)
        return {"data": data}, 200

    if request.method == 'POST':
        from api import db

        title = request.values.get('title')
        image_url = request.values.get('image_url')
        image_year = request.values.get('image_year')
        artist_name = request.values.get('artist_name')
        image_description = request.values.get('image_description')

        # Required Fields: title, image_url, image_year, artist_name, image_description
        if not (title and image_url and image_year and artist_name and image_description):
            return {"error": "title, image_url, image_year, artist_name, image_description are required parameters"}, 422

        artist = Artist.query.filter(Artist.name == artist_name).first()
        if not artist:
            return {"error": "artist_name not found, artist_name should be in our artists database to add new image."}, 422

        new_image = Image(
            title=title,
            image_url=image_url,
            artist=artist,
            year=image_year,
            description=image_description
        )

        db.session.add(new_image)

        try:
            db.session.commit()
            data = {}
            data['id'] = new_image.id
            data['image_url'] = new_image.image_url
            data['title'] = new_image.title
            data['year'] = new_image.year
            data['artist_id'] = new_image.artist_id
            data['artist_name'] = new_image.artist.name
            data['description'] = new_image.description
            data['artist_href'] = \
                request.host_url[:-1] + url_for('artists_api.artists_detail', artist_id=new_image.artist.id)
            return {"data": data}, 201

        except Exception:
            return {"error": "title, image_url, description should be string, year should be integer"}, 422
