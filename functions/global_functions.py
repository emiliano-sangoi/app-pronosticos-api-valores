


def get_error_response(msg):
    return crear_response(0, msg)


def crear_response(ok=1, msg=''):
    return {
        "ok" : ok,
        "msg" : msg
    }