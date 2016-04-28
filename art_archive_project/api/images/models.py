from api import db


class Image(db.Model):

    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    description = db.Column(db.String(255))

    def __init__(self, title=None, image_url=None, artist=None, **image_info):
        self.image_url = image_url
        self.title = title
        self.year = image_info.get('year', None)
        self.artist = artist
        self.description = image_info.get('description', None)

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
