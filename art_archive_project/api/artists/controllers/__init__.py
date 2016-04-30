from flask import Blueprint


# Define URL blueprint for artists endpoints
artists_api = Blueprint('artists_api', __name__, url_prefix='/artists')


# import controller for endpoints
from .artists import artists_list_get, artists_list_post
from .artists_detail import artists_detail
from .artists_artworks import artists_artworks
from .artists_search import artists_search
