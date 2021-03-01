from politylink.nlp.keyphrase import KeyPhraseExtractor


class TestKeyPhraseExtractor:
    def test_extract(self):
        extractor = KeyPhraseExtractor()
        assert ['日本犬', '世界中'] == extractor.extract(text='柴犬は日本犬の一種であり、世界中で人気の犬種です。', n=2)
