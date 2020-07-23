from politylink.graphql import hello


def test_hello():
    assert hello() == 'graphql'
