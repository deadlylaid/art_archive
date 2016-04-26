from api import db
from api.artists.models import Artist


class Image(db.Model):

    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship(
        Artist,
        backref=db.backref('images', lazy='dynamic'),
    )
    description = db.Column(db.String(255))

    def __init__(self, title=None, image_url=None, artist=None, **image_info):
        self.image_url = image_url
        self.title = title
        self.year = image_info.get('year', None)
        self.artist = artist
        self.description = image_info.get('description', None)

    def __repr__(self):
        return '<Image: {}>'.format(self.title)
