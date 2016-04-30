from api.artists.models import Artist
from api.utils.errors import unprocessable_entry


def get_filtered_query_result(query, params):
    if 'name' in params:
        query = query.filter(Artist.name.contains(params['name']))
    if 'country' in params:
        query = query.filter(Artist.country.contains(params['country']))
    if 'genre' in params:
        query = query.filter(Artist.genre.contains(params['genre']))
    if 'alive_in' in params:
        query = query.filter(Artist.birth_year <= params['alive_in']).\
                                        filter(or_(Artist.death_year == None, Artist.death_year >= params['alive_in']))
    if 'order' in params:
        order = params.get('order', 'asc')
        if order == "asc":
            query = query.order_by(Artist.created_at)
        elif order == "desc":
            query = query.order_by(-Artist.created_at)
        else:
            return None, unprocessable_entry("order parameter invalid, try desc or asc")
    if 'max_items' in params and params['max_items'].isdigit():
        query = query.limit(params['max_items'])
    return query.all(), None
