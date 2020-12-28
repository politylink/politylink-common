from politylink.helpers.abstract_finder import extract_texts


def test_extract_texts():
    assert [] == extract_texts(None)
    assert ['a'] == extract_texts('a')
    assert ['a', 'b'] == extract_texts(['a', 'b', 1])
    assert ['a', 'b', 'c'] == extract_texts(['a', ['b', 'c']])
