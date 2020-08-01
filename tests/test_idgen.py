import pytest

from politylink.idgen import idgen, Member


def test_idgen():
    assert idgen('test') == 'str:CY9rzUYh03PK3k6DJie09g'
    assert idgen('test') == idgen('test')
    assert idgen('test') != idgen('test2')

    member = Member(None)
    member.name = 'test'
    assert idgen(member) == 'Member:CY9rzUYh03PK3k6DJie09g'


def test_idgen_fail():
    with pytest.raises(ValueError):
        idgen('')

    with pytest.raises(ValueError):
        idgen(dict())
