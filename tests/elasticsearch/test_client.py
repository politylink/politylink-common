import pytest

from politylink.elasticsearch.client import ElasticsearchClient, ElasticsearchException, OpType
from politylink.elasticsearch.schema import BillText, NewsText, MinutesText, SpeechText


class TestGraphQLClient:
    bill_texts = [
        BillText({'id': 'Bill:1', 'title': '猫法改正案'}),
        BillText({'id': 'Bill:3', 'title': '犬法改正案'})
    ]
    news_texts = [
        NewsText({'id': 'News:1', 'title': 'ネコちゃんニュース', 'date': '2020-01-01'}),
        NewsText({'id': 'News:2', 'title': 'ワンちゃんニュース', 'date': '2021-01-01'})
    ]
    minutes_texts = [
        MinutesText({'id': 'Minutes:1', 'title': '猫委員会', 'body': '吾輩は猫である。'})
    ]
    speech_texts = [
        SpeechText({'id': 'Speech:1', 'title': '犬委員会', 'speaker': '柴犬', 'body': '会議を始めます'})
    ]

    def test_index(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            client.index(bill_text)
            client.index(bill_text, op_type=OpType.UPDATE)
            client.index(bill_text, op_type=OpType.SAFE_INDEX)
        for news_text in self.news_texts:
            client.index(news_text)
        for minutes_text in self.minutes_texts:
            client.index(minutes_text)
        for speech_text in self.speech_texts:
            client.index(speech_text)

    def test_bulk_index(self):
        client = ElasticsearchClient()
        client.bulk_index(self.bill_texts)
        client.bulk_index(self.bill_texts, op_type=OpType.UPDATE)

    def test_get(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            res = client.get(bill_text.id)
            assert bill_text.title == res.title
        for news_text in self.news_texts:
            res = client.get(news_text.id)
            assert news_text.title == res.title
        for minutes_text in self.minutes_texts:
            res = client.get(minutes_text.id)
            assert minutes_text.title == res.title
        for speech_text in self.speech_texts:
            res = client.get(speech_text.id)
            assert speech_text.title == res.title

    def test_get_fail(self):
        client = ElasticsearchClient()
        with pytest.raises(ElasticsearchException):
            client.get('Bill:1000')

    def test_exists(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            res = client.exists(bill_text.id)
            assert res
        assert not client.exists('Bill:1000')

    def test_search(self):
        client = ElasticsearchClient()
        assert len(client.search(NewsText))
        assert len(client.search(NewsText, query='ネコ'))
        assert 1 == len(client.search(NewsText, query='ネコ', start_date_str='2020-01-01', end_date_str='2020-01-02'))
        assert 0 == len(client.search(NewsText, query='ネコ', start_date_str='2020-01-02', end_date_str='2020-01-03'))

    def test_get_term_statistics(self):
        client = ElasticsearchClient()
        minutes_id = self.minutes_texts[0].id
        term2stats = client.get_term_statistics(minutes_id)
        assert '吾輩' in term2stats
        assert 1 == term2stats['吾輩']['tf']
