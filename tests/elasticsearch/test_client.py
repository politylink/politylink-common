import pytest

from politylink.elasticsearch.client import ElasticsearchClient, ElasticsearchException
from politylink.elasticsearch.schema import BillText, NewsText


class TestGraphQLClient:
    bill_texts = [
        BillText({'id': 'Bill:1', 'title': '猫法改正案'}),
        BillText({'id': 'Bill:3', 'title': '犬法改正案'})
    ]
    news_texts = [
        NewsText({'id': 'News:1', 'title': 'ネコちゃんニュース'})
    ]

    def test_index(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            client.index(bill_text)
        for news_text in self.news_texts:
            client.index(news_text)

    def test_get(self):
        client = ElasticsearchClient()
        for bill_text in self.bill_texts:
            res = client.get(bill_text.id)
            assert bill_text.title == res.title
        for news_text in self.news_texts:
            res = client.get(news_text.id)
            assert news_text.title == res.title

    def test_get_fail(self):
        client = ElasticsearchClient()
        with pytest.raises(ElasticsearchException):
            client.get('Bill:1000')

    def test_search(self):
        client = ElasticsearchClient()
        assert len(client.search(BillText))
        assert len(client.search(BillText, '猫'))
        assert len(client.search(NewsText))
