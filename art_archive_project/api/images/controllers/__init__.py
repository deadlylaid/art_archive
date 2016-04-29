from flask import Blueprint


# Define URL blueprint for artists endpoints
images_api = Blueprint('images_api', __name__, url_prefix='/images')


# import controller for endpoints
from .images import images_list
from .images_detail import images_detail
from .images_search import images_search
