from api.images.models import Image
from api.utils.errors import unprocessable_entry
from api.utils.response_wrapper import created_response


def create_new_image(database, artist=None, **params):
    new_image = Image(artist=artist, **params)
    database.session.add(new_image)
    try:
        database.session.commit()
        data = new_image.to_json_with_detail
        return created_response(data)
    except Exception:
        return unprocessable_entry("title, image_url, image_description should be string, year should be integer")
