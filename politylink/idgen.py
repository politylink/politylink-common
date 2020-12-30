import base64
import hashlib

from politylink.graphql.schema import *

"""
Minimal content based ID generator

ID = ${class}:${base}
$class = class name
$base = URL-safe base64 string of MD5 hash (length = 22)
"""


def idgen(obj):
    class_ = obj.__class__.__name__
    if isinstance(obj, str):
        base = _basegen_str(obj)
    elif isinstance(obj, Bill):
        base = _basegen_bill(obj)
    elif isinstance(obj, Law):
        base = _basegen_law(obj)
    elif isinstance(obj, Url) or isinstance(obj, News):
        base = _basegen_url(obj.url)
    elif isinstance(obj, Timeline):
        base = _basegen_timeline(obj)
    elif isinstance(obj, Minutes):
        base = _basegen_minutes(obj)
    elif isinstance(obj, Speech):
        base = _basegen_speech(obj)
    elif isinstance(obj, Diet):
        base = _basegen_diet(obj)
    elif isinstance(obj, Activity):
        base = _basegen_activity(obj)
    elif hasattr(obj, 'name'):
        base = _basegen_str(getattr(obj, 'name'))
    else:
        raise ValueError(f'can not calculate ID for {class_}')
    return f'{class_}:{base}'


def _basegen_str(s: str):
    if not s:
        raise ValueError(f'non-empty string is required to calculate ID')
    h = hashlib.md5()
    h.update(s.encode('UTF-8'))
    b = base64.b64encode(h.digest(), altchars=b'-_')
    return b.decode('UTF-8')[:-2]  # last 2 bit is always padding (=)


def _basegen_bill(bill: Bill):
    return _basegen_str(bill.bill_number)


def _basegen_law(law: Law):
    return _basegen_str(law.law_number)


def _basegen_url(url: str):
    protocol, body = url.split('://')
    return _basegen_str(body)


def _basegen_timeline(timeline: Timeline):
    dt = timeline.date
    return f'{dt.year:04}{dt.month:02}{dt.day:02}'


def _basegen_minutes(minutes: Minutes):
    dt = minutes.start_date_time
    dt_str = f'{dt.year:04}{dt.month:02}{dt.day:02}'
    return _basegen_str(minutes.name + dt_str)


def _basegen_speech(speech: Speech):
    return _basegen_str(f'{speech.minutes_id}{speech.order_in_minutes}')


def _basegen_diet(diet: Diet):
    return diet.number


def _basegen_activity(activity: Activity):
    id_str = ''
    for id_field in ['member_id', 'bill_id', 'minutes_id']:  # order matters
        if hasattr(activity, id_field):
            id_str += getattr(activity, id_field)
    dt = activity.datetime
    dt_str = f'{dt.year:04}{dt.month:02}{dt.day:02}'
    return _basegen_str(f'{id_str}{dt_str}')
