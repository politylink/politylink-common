from datetime import datetime, date

import pytest

from politylink.graphql.schema import _Neo4jDateTimeInput
from politylink.utils import DateConverter, filter_dict_by_value, filter_dict_by_thresh, contains_word, get_str_offset, \
    convert_kansuji_to_int, deduplicate, replace_kansuji_to_number, to_date_str, strip_join


def test_to_date_str():
    assert to_date_str(date(2020, 1, 1)) == '2020-01-01'
    assert to_date_str(_Neo4jDateTimeInput(year=2020, month=1, day=1)) == '2020-01-01'


def test_filter_dict_by_value():
    data = {'a': 1, 'b': 3, 'c': 2}
    filtered = filter_dict_by_value(data, num_items=2)
    assert set(filtered.keys()) == {'b', 'c'}


def test_filter_dict_by_thresh():
    data = {'a': 1, 'b': 3, 'c': 2}
    filtered = filter_dict_by_thresh(data, thresh=2)
    assert set(filtered.keys()) == {'b', 'c'}


def test_contains_word():
    assert not contains_word('')
    assert not contains_word('', allow_list=['テキスト'])
    assert not contains_word('テキストを含む')
    assert contains_word('テキストを含む', allow_list=['おにぎり', 'テキスト'])
    assert contains_word('おにぎり', allow_list=['おにぎり'])
    assert not contains_word('テキストを含む', allow_list=['テキスト'], block_list=['含む'])


def test_strip_join():
    assert strip_join(['  aaa  ', 'bbb', 'ccc ']) == 'aaabbbccc'


def test_deduplicate():
    assert deduplicate([]) == []
    assert deduplicate(['aaa', 'bbb']) == ['aaa', 'bbb']
    assert deduplicate(['aaa', 'bbb', 'ccc', 'aaa', 'ddd', 'bbb']) == ['aaa', 'bbb', 'ccc', 'ddd']


def test_convert_kansuji_to_int():
    assert convert_kansuji_to_int('一〇') == 10
    assert convert_kansuji_to_int('四二') == 42
    assert convert_kansuji_to_int('百') == 100
    assert convert_kansuji_to_int('百九十六') == 196
    assert convert_kansuji_to_int('一九六') == 196
    assert convert_kansuji_to_int('千二') == 1002
    assert convert_kansuji_to_int('千十') == 1010
    assert convert_kansuji_to_int('千十六') == 1016
    assert convert_kansuji_to_int('千九十六') == 1096


def test_convert_kansuji_to_int_fail():
    with pytest.raises(ValueError):
        assert convert_kansuji_to_int('百千')

    with pytest.raises(ValueError):
        assert convert_kansuji_to_int('犬百')


def test_replace_kansuji_to_number():
    assert replace_kansuji_to_number('第百九十六回国会衆法第四二号') == '第196回国会衆法第42号'


def test_get_str_offset():
    assert get_str_offset('') == -1
    assert get_str_offset('   ') == -1
    assert get_str_offset('   こんにちは') == 3


class TestDateConverter:
    def test_convert(self):
        assert DateConverter.convert('令和元年10月11日') == datetime(year=2019, month=10, day=11)
        assert DateConverter.convert('令和2年一　月 ２日') == datetime(year=2020, month=1, day=2)
        assert DateConverter.convert('開会年月日　令和2年7月9日(閉会後)') == datetime(year=2020, month=7, day=9)
