from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Base Flask app settings
app = Flask(__name__)
app.config.from_object('config')

# For database abstraction
db = SQLAlchemy(app)

# urls patterns
from api.test_api.controllers import test_api as test_api_urls

# Register blueprints
app.register_blueprint(test_api_urls)
