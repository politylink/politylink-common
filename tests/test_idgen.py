import pytest

from politylink.graphql.schema import Member, Timeline, _Neo4jDateTimeInput, Minutes, Activity
from politylink.idgen import idgen, _basegen_str, _basegen_url, _basegen_minutes, _basegen_activity


def test_idgen():
    assert idgen('test') == 'str:CY9rzUYh03PK3k6DJie09g'
    assert idgen('test') == idgen('test')
    assert idgen('test') != idgen('test2')

    member = Member({'name': 'test'})
    assert idgen(member) == 'Member:CY9rzUYh03PK3k6DJie09g'

    timeline = Timeline(None)
    timeline.date = _Neo4jDateTimeInput(year=2020, month=2, day=20)
    assert idgen(timeline) == 'Timeline:20200220'


def test_idgen_fail():
    with pytest.raises(ValueError):
        idgen('')

    with pytest.raises(ValueError):
        idgen(dict())


def test_basegen_url():
    url = 'https://kokkai.ndl.go.jp/#/detail?minId=120105254X03220200610'
    assert _basegen_url(url) == _basegen_str('kokkai.ndl.go.jp/#/detail?minId=120105254X03220200610')


def test_basegen_minutes():
    minutes = Minutes({'name': '参議院災害対策特別委員会'})
    minutes.start_date_time = _Neo4jDateTimeInput(year=2020, month=1, day=20)
    assert _basegen_minutes(minutes) == _basegen_str('参議院災害対策特別委員会20200120')


def test_basegen_activity():
    activity = Activity(None)
    activity.member_id = 'Member:id'
    activity.minutes_id = 'Minutes:id'
    activity.datetime = _Neo4jDateTimeInput(year=2020, month=1, day=20)
    assert _basegen_activity(activity) == _basegen_str('Member:idMinutes:id20200120')
