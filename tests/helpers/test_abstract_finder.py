from politylink.graphql.schema import Bill
from politylink.helpers.abstract_finder import extract_texts, is_text_match


def test_extract_texts():
    assert [] == extract_texts(None)
    assert ['a'] == extract_texts('a')
    assert ['a', 'b'] == extract_texts(['a', 'b', 1])
    assert ['a', 'b', 'c'] == extract_texts(['a', ['b', 'c']])


def test_is_text_match():
    search_fields = ['name', 'aliases']

    assert is_text_match(Bill({'name': '法律案A'}), search_fields, text='法律案', exact_match=False)
    assert is_text_match(Bill({'name': '法律案A'}), search_fields, text='法律案A', exact_match=True)
    assert not is_text_match(Bill({'name': '法律案A'}), search_fields, text='法律案', exact_match=True)
    assert is_text_match(Bill({'aliases': ['猫ちゃん', '法律案']}), search_fields, text='法律案', exact_match=True)
    assert not is_text_match(Bill({'aliases': ['法律', '案']}), search_fields, text='法律案', exact_match=True)
