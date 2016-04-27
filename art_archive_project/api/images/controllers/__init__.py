from flask import Blueprint


# Define URL blueprint for artists endpoints
images_api = Blueprint('images_api', __name__, url_prefix='/images')


# import controller for endpoints
from .images import images_list
