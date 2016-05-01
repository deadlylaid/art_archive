from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Base Flask app settings
app = Flask(__name__)
app.config.from_object('config')

# For database abstraction
db = SQLAlchemy(app)

# urls patterns
from api.test_api.controllers import test_api as test_api_urls
from api.artists.controllers import artists_api as artists_api_urls
from api.images.controllers import images_api as images_api_urls

# Register blueprints
app.register_blueprint(test_api_urls)
app.register_blueprint(artists_api_urls)
app.register_blueprint(images_api_urls)
