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
        assert 'Bill' in data['data']

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_bill(self):
        client = GraphQLClient()
        bill = self._build_sample_bill()
        merged_bill = client.exec_merge_bill(bill)
        assert merged_bill.id == bill.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_url(self):
        client = GraphQLClient()
        url = self._build_sample_url()
        merged_url = client.exec_merge_url(url)
        assert merged_url.id == url.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_minutes(self):
        client = GraphQLClient()
        minutes = self._build_sample_minutes()
        merged_minutes = client.exec_merge_minutes(minutes)
        assert merged_minutes.id == minutes.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_committee(self):
        client = GraphQLClient()
        committee = self._build_sample_committee()
        merged_committee = client.exec_merge_committee(committee)
        assert merged_committee.id == committee.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_speech(self):
        client = GraphQLClient()
        speech = self._build_sample_speech()
        merged_speech = client.exec_merge_speech(speech)
        assert merged_speech.id == speech.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_url_referred_bills(self):
        client = GraphQLClient()
        url = self._build_sample_url()
        bill = self._build_sample_bill()
        res = client.exec_merge_url_referred_bills(url.id, bill.id)
        assert res.from_.id == url.id
        assert res.to.id == bill.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_speech_belonged_to_minutes(self):
        client = GraphQLClient()
        speech = self._build_sample_speech()
        minutes = self._build_sample_minutes()
        res = client.exec_merge_speech_belonged_to_minutes(speech.id, minutes.id)
        assert res.from_.id == speech.id
        assert res.to.id == minutes.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_minutes_discussed_bills(self):
        client = GraphQLClient()
        minutes = self._build_sample_minutes()
        bill = self._build_sample_bill()
        res = client.exec_merge_minutes_discussed_bills(minutes.id, bill.id)
        assert res.from_.id == minutes.id
        assert res.to.id == bill.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_minutes_belonged_to_committee(self):
        client = GraphQLClient()
        minutes = self._build_sample_minutes()
        committee = self._build_sample_committee()
        res = client.exec_merge_minutes_belonged_to_committee(minutes.id, committee.id)
        assert res.from_.id == minutes.id
        assert res.to.id == committee.id

    def test_show_all_ops(self):
        bill = self._build_sample_bill()
        url = self._build_sample_url()
        minutes = self._build_sample_minutes()
        committee = self._build_sample_committee()
        speech = self._build_sample_speech()
        LOGGER.warning(GraphQLClient._build_all_bills_operation())
        LOGGER.warning(GraphQLClient._build_all_committees_operation())
        LOGGER.warning(GraphQLClient._build_merge_bill_operation(bill))
        LOGGER.warning(GraphQLClient._build_merge_url_operation(url))
        LOGGER.warning(GraphQLClient._build_merge_minutes_operation(minutes))
        LOGGER.warning(GraphQLClient._build_merge_committee_operation(committee))
        LOGGER.warning(GraphQLClient._build_merge_speech_operation(speech))
        LOGGER.warning(GraphQLClient._build_merge_url_referred_bills(url.id, bill.id))
        LOGGER.warning(GraphQLClient._build_merge_speech_belonged_to_minutes(speech.id, minutes.id))
        LOGGER.warning(GraphQLClient._build_merge_minutes_discussed_bills(minutes.id, bill.id))
        LOGGER.warning(GraphQLClient._build_merge_minutes_belonged_to_committee(minutes.id, committee.id))

    @staticmethod
    def _build_sample_bill():
        bill = Bill(None)
        bill.name = '公文書等の管理に関する法律の一部を改正する法律案'
        bill.bill_number = '第195回衆法第4号'
        bill.submitted_date = _Neo4jDateTimeInput(year=2020, month=1, day=1)
        bill.id = idgen(bill)
        bill.invalid_field = 'このfieldはmerge_billに使われない'
        return bill

    @staticmethod
    def _build_sample_url():
        url = Url(None)
        url.url = 'http://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/honbun/g19505004.htm'
        url.id = idgen(url)
        return url

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
