def ok_response(data, msg=None, **verbose):
    max_items = verbose.get('max_items', '')
    if max_items.isdigit() and int(max_items) > len(data):
        msg = "requested with max_items: \
            {0} but only {1} items were found \
            matching the query".format(max_items, len(data))
    if not data:
        msg = "No results were retrieved from database"
    if msg:
        meta = {"response_msg": msg}
        return {"data": data, "meta": meta}, 200
    return {"data": data}, 200


def created_response(data):
    return {"data": data}, 201
