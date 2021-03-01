from politylink.nlp.keyphrase import KeyPhraseExtractor


class TestKeyPhraseExtractor:
    def test_extract(self):
        extractor = KeyPhraseExtractor()
        assert ['猫', '元気'] == extractor.get_key_phrase(text='今日も猫ちゃんは元気に庭を走り回っています', n=2)
