from datetime import datetime

import pytest

from politylink.graphql.schema import Member, Url, Timeline, _Neo4jDateTimeInput
from politylink.idgen import idgen, _basegen_str, _basegen_url, _basegen_timeline


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
