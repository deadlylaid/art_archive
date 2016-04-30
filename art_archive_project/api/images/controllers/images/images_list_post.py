from flask import request

from api import db
from api.images.models import Image
from api.artists.models import Artist
from api.images.controllers import images_api
from api.utils.json_decorator import json
from api.utils.errors import unprocessable_entry
from api.utils.nullify import nullify
from api.images.utils import create_new_image


@images_api.route("/", methods=['POST'])
@json
def images_list_post():
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
    return create_new_image(db, artist=artist, **params)
