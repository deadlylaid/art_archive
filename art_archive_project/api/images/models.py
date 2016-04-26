from api import db


class Image(db.Model):

    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer)
    description = db.Column(db.String(255))

    def __init__(self, title=None, image_url=None, **image_info):
        self.image_url = image_url
        self.title = title
        self.year = image_info.get('year', None)
        self.artist_id = image_info.get('artist_id', None)
        self.description = image_info.get('description', None)

    def __repr__(self):
        return '<Image: {}>'.format(self.title)
