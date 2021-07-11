import pytest

from politylink.graphql.schema import ParliamentaryGroup
from politylink.graphql.utils import to_parliamentary_group


def test_to_parliamentary_group():
    assert to_parliamentary_group('自民') == ParliamentaryGroup.JIMIN
    assert to_parliamentary_group('自由民主党・無所属の会') == ParliamentaryGroup.JIMIN
    assert to_parliamentary_group('立民') == ParliamentaryGroup.RIKKEN
    assert to_parliamentary_group('立憲民主党・無所属') == ParliamentaryGroup.RIKKEN

    with pytest.raises(ValueError):
        assert to_parliamentary_group('ウサイン・ボルト')
