from datetime import datetime
from api import db
from api.utils.url_helper import get_absolute_url
from api.utils.errors import unprocessable_entry


class Artist(db.Model):

    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    country = db.Column(db.String(45))
    genre = db.Column(db.String(45))
    images = db.relationship(
        'Image',
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

    
    @classmethod
    def filter_by_params(cls, params):
        query = cls.query
        if 'name' in params:
            query = cls.filter_by_name(query, params['name'])
        if 'country' in params:
            query = cls.filter_by_country(query, params['country'])
        if 'genre' in params:
            query = cls.filter_by_genre(query, params['genre'])
        if 'alive_in' in params:
            query = cls.filter_by_alive_in(query, params['alive_in'])
        if 'order' in params:
            query, error = cls.filter_by_order(query, params['order'])
            if error: return None, error
        if 'max_items' in params:
            query = cls.filter_by_max_items(query, params['max_items'])
        return query.all(), None


    @classmethod
    def filter_by_name(cls, query, name): 
        return query.filter(cls.name.contains(name))


    @classmethod
    def filter_by_country(cls, query, country): 
        return query.filter(cls.country.contains(country))


    @classmethod
    def filter_by_genre(cls, query, genre): 
        return query.filter(cls.genre.contains(genre))


    @classmethod
    def filter_by_alive_in(cls, query, alive_in): 
        return query.filter(cls.birth_year <= alive_in).\
                                        filter(or_(cls.death_year == None, cls.death_year >= alive_in))


    @classmethod
    def filter_by_order(cls, query, order): 
        if not order in ['desc', 'asc']:
            return None, unprocessable_entry("order parameter invalid, try desc or asc")
        if order == 'desc':
            return query.order_by(-cls.created_at), None
        return query.order_by(cls.created_at), None


    @classmethod
    def filter_by_max_items(cls, query, max_items): 
        if max_items.isdigit():
            return query.limit(max_items)
        return query


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
