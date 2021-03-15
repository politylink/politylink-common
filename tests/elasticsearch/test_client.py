import pytest

from politylink.elasticsearch.client import ElasticsearchClient, ElasticsearchException
from politylink.elasticsearch.schema import BillText, NewsText, MinutesText


class TestGraphQLClient:
    bill_texts = [
        BillText({'id': 'Bill:1', 'title': '猫法改正案'}),
        BillText({'id': 'Bill:3', 'title': '犬法改正案'})
    ]
    news_texts = [
        NewsText({'id': 'News:1', 'title': 'ネコちゃんニュース'})
    ]
    minutes_texts = [
        MinutesText(
            {'id': 'Minutes:1', 'title': '猫委員会', 'body': '吾輩は猫である。'})
    ]

    def test_index(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            client.index(bill_text)
        for news_text in self.news_texts:
            client.index(news_text)
        for minutes_text in self.minutes_texts:
            client.index(minutes_text)

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

    def test_get_fail(self):
        client = ElasticsearchClient()
        with pytest.raises(ElasticsearchException):
            client.get('Bill:1000')

    def test_search(self):
        client = ElasticsearchClient()
        assert len(client.search(BillText))
        assert len(client.search(BillText, '猫'))
        assert len(client.search(NewsText))

    def test_get_term_statistics(self):
        client = ElasticsearchClient()
        minutes_id = self.minutes_texts[0].id
        term2stats = client.get_term_statistics(minutes_id)
        assert '吾輩' in term2stats
        assert 1 == term2stats['吾輩']['tf']
