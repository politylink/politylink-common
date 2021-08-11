from politylink.nlp.utils import filter_by_pos, MatchMode


def test_filter_by_pos():
    assert filter_by_pos(['猫', 'こんにちは', 'その犬', '犬が走る'], pos_tags=['NOUN'], mode=MatchMode.ANY) == ['猫', 'その犬', '犬が走る']
    assert filter_by_pos(['猫', 'こんにちは', 'その犬', '犬が走る'], pos_tags=['NOUN'], mode=MatchMode.ALL) == ['猫']
    assert filter_by_pos(['猫', 'こんにちは', 'その犬', '犬が走る'], pos_tags=['NOUN'], mode=MatchMode.LAST) == ['猫', 'その犬']
