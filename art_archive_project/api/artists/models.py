from datetime import datetime
from api import db
from api.images.models import Image
from api.utils.url_helper import get_absolute_url


class Artist(db.Model):

    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    country = db.Column(db.String(45))
    genre = db.Column(db.String(45))
    images = db.relationship(
        Image,
        backref=db.backref('artist'),
    )
    created_at = db.Column(db.DateTime(timezone=False))
    updated_at = db.Column(db.DateTime(timezone=False))

    def __init__(self, **artist_info):
        self.name = artist_info.get('name')
        self.country = artist_info.get('country')
        self.genre = artist_info.get('genre')
        self.birth_year = artist_info.get('birth_year')
        self.death_year = artist_info.get('death_year')
        self.created_at = datetime.now()


    def __repr__(self):
        return '<Artist: {}>'.format(self.name)


    @property
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'death_year': self.death_year,
            'country': self.country,
            'genre': self.genre,
        }


    @property
    def to_json_with_detail(self):
        data = self.to_json
        data['detail_href'] = get_absolute_url('artists_api.artists_detail', artist_id=self.id)
        return data


    @property
    def to_json_with_artworks(self):
        data = self.to_json
        data['artworks_href'] = get_absolute_url('artists_api.artists_artworks', artist_id=self.id)
        return data
