import base64
import hashlib
from urllib.parse import urlparse

from politylink.graphql.schema import *

"""
Minimal content based ID generator in form of ${class}:${base}

$class = class name
$base = base64 string of MD5 hash (length = 22)
"""


def idgen(obj):
    if isinstance(obj, str):
        base = _basegen_str(obj)
    elif isinstance(obj, Bill):
        base = _basegen_bill(obj)
    elif isinstance(obj, Law):
        base = _basegen_law(obj)
    elif isinstance(obj, Url):
        base = _basegen_url(obj)
    elif hasattr(obj, 'name'):
        base = _basegen_str(getattr(obj, 'name'))
    else:
        base = _basegen_str(str(obj))
    return f'{obj.__class__.__name__}:{base}'


def _basegen_str(s):
    h = hashlib.md5()
    h.update(s.encode('UTF-8'))
    b = base64.b64encode(h.digest())
    return b.decode('UTF-8')[:-2]  # last 2 bit is always padding (=)


def _basegen_bill(bill):
    return _basegen_str(bill.bill_number)


def _basegen_law(law):
    return _basegen_str(law.law_number)


def _basegen_url(url):
    o = urlparse(url.url)
    return _basegen_str(o.netloc + o.path)
