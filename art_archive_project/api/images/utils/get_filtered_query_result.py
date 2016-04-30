from api.artists.models import Artist
from api.images.models import Image
from api.utils.errors import unprocessable_entry


def get_filtered_query_result(query, params):
    if 'title' in params:
        query = query.filter(Image.title.contains(params['title']))
    if 'year' in params:
        query = query.filter(Image.year == params['year'])
    if 'artist_name' in params:
        query = query.join(Image.artist).filter(Artist.name.contains(params['artist_name']))
    if 'genre' in params:
        query = query.join(Image.artist).filter(Artist.genre.contains(params['genre']))
    if 'description' in params:
        query = query.filter(Image.description.contains(params['description']))
    if 'order' in params:
        order = params.get('order', 'asc')
        if order == "asc":
            query = query.order_by(Image.year)
        elif order == "desc":
            query = query.order_by(-Image.year)
        else:
            return None, unprocessable_entry("order parameter invalid, try desc or asc")
    if 'max_items' in params and params['max_items'].isdigit():
        query = query.limit(params['max_items'])
    return query.all(), None
