from datetime import datetime
from api import db


class Artist(db.Model):

    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    country = db.Column(db.String(45))
    genre = db.Column(db.String(45))
    created_at = db.Column(db.DateTime(timezone=False))
    updated_at = db.Column(db.DateTime(timezone=False))

    def __init__(self, name=None, **artist_info):
        self.name = name
        self.birth_year = artist_info.get('birth_year', None)
        self.death_year = artist_info.get('death_year', None)
        self.country = artist_info.get('country', None)
        self.genre = artist_info.get('genre', None)
        self.created_at = datetime.now()

    def __repr__(self):
        return '<Artist: {}>'.format(self.name)
