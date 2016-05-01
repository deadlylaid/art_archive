from api import db
from api.utils.url_helper import get_absolute_url
from api.utils.errors import unprocessable_entry
from api.artists.models import Artist


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


    @classmethod
    def filter_by_params(cls, params): 
        query = cls.query
        if 'title' in params:
            query = cls.filter_by_title(query, params['title'])
        if 'year' in params:
            query = cls.filter_by_year(query, params['year'])
        if 'artist_name' in params:
            query = cls.filter_by_artist_name(query, params['artist_name'])
        if 'genre' in params:
            query = cls.filter_by_genre(query, params['genre'])
        if 'description' in params:
            query = cls.filter_by_description(query, params['description'])
        if 'order' in params:
            query, error = cls.filter_by_order(query, params['order'])
            if error: return None, error
        if 'max_items' in params:
            query = cls.filter_by_max_items(query, params['max_items'])
        return query.all(), None


    @classmethod
    def filter_by_title(cls, query, title): 
        return query.filter(cls.title.contains(title))


    @classmethod
    def filter_by_year(cls, query, year): 
        return query.filter(cls.year == year)


    @classmethod
    def filter_by_artist_name(cls, query, artist_name): 
        return query.join(cls.artist).filter(Artist.name.contains(artist_name))


    @classmethod
    def filter_by_genre(cls, query, genre): 
        return query.join(cls.artist).filter(Artist.genre.contains(genre))


    @classmethod
    def filter_by_description(cls, query, description): 
        return query.filter(cls.description.contains(description))


    @classmethod
    def filter_by_order(cls, query, order): 
        if not order in ['desc', 'asc']:
            return None, unprocessable_entry("order parameter invalid, try desc or asc")
        if order == 'desc':
            return query.order_by(-cls.year), None
        return query.order_by(cls.year), None


    @classmethod
    def filter_by_max_items(cls, query, max_items): 
        if max_items.isdigit():
            return query.limit(max_items)
        return query


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


    @property
    def to_json_with_artist(self):
        data = self.to_json
        data['artist_href'] = get_absolute_url('artists_api.artists_detail', artist_id=self.artist.id)
        return data


    @property
    def to_json_search_result(self):
        data = self.to_json
        data['detail_href'] = get_absolute_url('images_api.images_detail', image_id=self.id)
        data['genre'] = self.artist.genre
        return data
