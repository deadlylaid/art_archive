from api import db
from api.utils.url_helper import get_absolute_url


class Image(db.Model):

    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    description = db.Column(db.String(255))

    def __init__(self, artist=None, **image_info):
        self.artist = artist
        self.image_url = image_info.get('image_url')
        self.title = image_info.get('title')
        self.year = image_info.get('image_year', None)
        self.description = image_info.get('image_description', None)

    def __repr__(self):
        return '<Image: {}>'.format(self.title)

    @property
    def to_json(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'year': self.year,
            'artist_id': self.artist.id,
            'artist_name': self.artist.name,
            'description': self.description,
        }


    @property
    def to_json_with_detail(self):
        data = self.to_json
        data['detail_href'] = get_absolute_url('images_api.images_detail', image_id=self.id)
        return data
