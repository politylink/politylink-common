from logging import getLogger

import pytest

from politylink.graphql import POLITYLINK_AUTH
from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import Bill

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
        assert len(data['data']['allBills']) > 0

    def test_exec_all_bills(self):
        client = GraphQLClient()
        bills = client.exec_all_bills()
        LOGGER.warning(bills)
        assert len(bills) > 0

    @pytest.mark.skipif(not POLITYLINK_AUTH, reason='requires authorization')
    def test_exec_merge_bill(self):
        client = GraphQLClient()
        bill = self._build_sample_bill()
        merged_bill = client.exec_merge_bill(bill)
        LOGGER.warning(merged_bill)
        assert merged_bill.id == bill.id

    def test_show_all_ops(self):
        LOGGER.warning(GraphQLClient._build_all_bills_operation())
        LOGGER.warning(GraphQLClient._build_merge_bill_operation(self._build_sample_bill()))

    @staticmethod
    def _build_sample_bill():
        bill = Bill(None)
        bill.id = 'bill:195-SYUHOU-4'
        bill.bill_title = '公文書等の管理に関する法律の一部を改正する法律案'
        bill.invalid_field = 'このfieldはmerge_billに使われない'
        return bill
