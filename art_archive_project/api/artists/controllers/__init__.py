from flask import Blueprint


# Define URL blueprint for artists endpoints
artists_api = Blueprint('artists_api', __name__, url_prefix='/artists')


# import controller for endpoints
from .artists import artists_list
from .artists_detail import artists_detail
from .artists_artworks import artists_artworks
