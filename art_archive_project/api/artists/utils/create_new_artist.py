from api.artists.models import Artist
from api.utils.url_helper import get_absolute_url
from api.utils.errors import unprocessable_entry
from api.utils.response_wrapper import created_response


def create_new_artist(database, **params):
    new_artist = Artist(**params)
    database.session.add(new_artist)
    try:
        database.session.commit()
        data = new_artist.to_json_with_detail
        return created_response(data)
    except Exception:
        return unprocessable_entry("name, country, genre should be string, birth_year, death_year should be integer")
