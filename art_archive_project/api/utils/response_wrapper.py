def ok_response(data, msg=None):
    if msg:
        meta = {"response_msg": msg}
        return {"data": data, "meta": meta}, 200
    return {"data": data}, 200


def created_response(data):
    return {"data": data}, 201
