import os


# Setting parameters for art_archive_project
DEBUG = True

# Host address, Port
HOST = '127.0.0.1'
PORT = 8000

# Base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# DATABASE URI
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/art_archive'
