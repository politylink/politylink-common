from logging import getLogger

import pytest

from politylink.graphql import POLITYLINK_AUTH
from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import *
from politylink.graphql.schema import _Neo4jDateTimeInput
from politylink.idgen import idgen

LOGGER = getLogger(__name__)


class TestGraphQLClient:
    def test_exec(self):
        client = GraphQLClient()
        query = """
        {
            Bill {
                name
                billNumber
            }
        }
        """
        data = client.exec(query)
        assert 'Bill' in data

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_merge(self):
        client = GraphQLClient()

        bill = self._build_sample_bill()
        data = client.merge(bill)
        assert data['MergeBill']['id'] == bill.id

        url = self._build_sample_url()
        data = client.merge(url)
        assert data['MergeUrl']['id'] == url.id

        news = self._build_sample_news()
        data = client.merge(news)
        assert data['MergeNews']['id'] == news.id

        minutes = self._build_sample_minutes()
        data = client.merge(minutes)
        assert data['MergeMinutes']['id'] == minutes.id

        committee = self._build_sample_committee()
        data = client.merge(committee)
        assert data['MergeCommittee']['id'] == committee.id

        speech = self._build_sample_speech()
        data = client.merge(speech)
        assert data['MergeSpeech']['id'] == speech.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_link(self):
        client = GraphQLClient()

        url = self._build_sample_url()
        bill = self._build_sample_bill()
        news = self._build_sample_news()
        speech = self._build_sample_speech()
        minutes = self._build_sample_minutes()
        committee = self._build_sample_committee()

        data = client.link(url.id, bill.id)
        assert data['MergeUrlReferredBills']['from']['id'] == url.id
        assert data['MergeUrlReferredBills']['to']['id'] == bill.id

        data = client.link(url.id, minutes.id)
        assert data['MergeUrlReferredMinutes']['from']['id'] == url.id
        assert data['MergeUrlReferredMinutes']['to']['id'] == minutes.id

        data = client.link(news.id, bill.id)
        assert data['MergeNewsReferredBills']['from']['id'] == news.id
        assert data['MergeNewsReferredBills']['to']['id'] == bill.id

        data = client.link(news.id, minutes.id)
        assert data['MergeNewsReferredMinutes']['from']['id'] == news.id
        assert data['MergeNewsReferredMinutes']['to']['id'] == minutes.id

        data = client.link(speech.id, minutes.id)
        assert data['MergeSpeechBelongedToMinutes']['from']['id'] == speech.id
        assert data['MergeSpeechBelongedToMinutes']['to']['id'] == minutes.id

        data = client.link(minutes.id, bill.id)
        assert data['MergeMinutesDiscussedBills']['from']['id'] == minutes.id
        assert data['MergeMinutesDiscussedBills']['to']['id'] == bill.id

        data = client.link(minutes.id, committee.id)
        assert data['MergeMinutesBelongedToCommittee']['from']['id'] == minutes.id
        assert data['MergeMinutesBelongedToCommittee']['to']['id'] == committee.id

    def test_show_ops(self):
        bill = self._build_sample_bill()
        url = self._build_sample_url()

        LOGGER.warning(GraphQLClient.build_merge_operation(bill))
        LOGGER.warning(GraphQLClient.build_link_operation(url.id, bill.id))
        LOGGER.warning(GraphQLClient.build_all_bills_operation())
        LOGGER.warning(GraphQLClient.build_all_committees_operation())

    @staticmethod
    def _build_sample_bill():
        bill = Bill(None)
        bill.name = '公文書等の管理に関する法律の一部を改正する法律案'
        bill.bill_number = '第195回衆法第4号'
        bill.invalid_field = 'このfieldはmerge_billに使われない'
        bill.submitted_date = _Neo4jDateTimeInput(year=2020, month=1, day=1)
        bill.id = idgen(bill)
        return bill

    @staticmethod
    def _build_sample_url():
        url = Url(None)
        url.url = 'http://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/honbun/g19505004.htm'
        url.id = idgen(url)
        return url

    @staticmethod
    def _build_sample_news():
        news = News(None)
        news.url = 'https://www.nikkei.com/article/DGXMZO64119940S0A920C2000000/'
        news.id = idgen(news)
        return news

    @staticmethod
    def _build_sample_minutes():
        minutes = Minutes(None)
        minutes.name = '第201回国会衆議院環境委員会第4号'
        minutes.topics = ["天気について", "カレーライスの件"]
        minutes.id = idgen(minutes)
        return minutes

    @staticmethod
    def _build_sample_speech():
        speech = Speech(None)
        speech.name = '第201回国会衆議院環境委員会第4号3'
        speech.id = idgen(speech)
        return speech

    @staticmethod
    def _build_sample_committee():
        committee = Committee(None)
        committee.name = '衆議院環境委員会'
        committee.topics = ['環境省の所管に属する事項']
        committee.id = idgen(committee)
        return committee
