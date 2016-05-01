from flask import request, url_for


def get_absolute_url(endpoint, **values):
    absolute_url = request.host_url[:-1] + url_for(endpoint, **values)
    return absolute_url
