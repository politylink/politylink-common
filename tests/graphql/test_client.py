from logging import getLogger

import pytest

from politylink.graphql import POLITYLINK_AUTH
from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import Bill, Url

LOGGER = getLogger(__name__)


class TestGraphQLClient:
    def test_exec(self):
        client = GraphQLClient()
        query = """{
            allBills {
                billTitle
            }
        }"""
        data = client.exec(query)
        LOGGER.warning(data)
        assert 'allBills' in data['data']

    def test_exec_all_bills(self):
        client = GraphQLClient()
        bills = client.exec_all_bills()
        LOGGER.warning(bills)
        assert len(bills) > 0

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_bill(self):
        client = GraphQLClient()
        bill = self._build_sample_bill()
        merged_bill = client.exec_merge_bill(bill)
        LOGGER.warning(merged_bill)
        assert merged_bill.id == bill.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_url(self):
        client = GraphQLClient()
        url = self._build_sample_url()
        merged_url = client.exec_merge_url(url)
        LOGGER.warning(merged_url)
        assert merged_url.id == url.id

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='authorization required')
    def test_exec_merge_url(self):
        client = GraphQLClient()
        url = self._build_sample_url()
        bill = self._build_sample_bill()
        res = client.exec_merge_url_referred_bills(url.id, bill.id)
        LOGGER.warning(res)
        assert res.from_.id == url.id
        assert res.to.id == bill.id

    def test_show_all_ops(self):
        bill = self._build_sample_bill()
        url = self._build_sample_url()
        LOGGER.warning(GraphQLClient._build_all_bills_operation())
        LOGGER.warning(GraphQLClient._build_merge_bill_operation(bill))
        LOGGER.warning(GraphQLClient._build_merge_url_operation(url))
        LOGGER.warning(GraphQLClient._build_merge_url_referred_bills(url.id, bill.id))

    @staticmethod
    def _build_sample_bill():
        bill = Bill(None)
        bill.name = '公文書等の管理に関する法律の一部を改正する法律案'
        bill.invalid_field = 'このfieldはmerge_billに使われない'
        return bill

    @staticmethod
    def _build_sample_url():
        url = Url(None)
        url.id = 'url:http://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/honbun/g19505004.htm'
        url.url = 'http://www.shugiin.go.jp/internet/itdb_gian.nsf/html/gian/honbun/g19505004.htm'
        return url
