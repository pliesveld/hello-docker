import functools
import json

def return_json(f):
    @functools.wraps(f)
    def inner(*a, **k):
        return json.dumps(f(*a, **k))
    return inner
