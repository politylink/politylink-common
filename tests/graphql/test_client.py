from logging import getLogger

import pytest

from politylink.graphql import GRAPHQL_AUTH
from politylink.graphql.client import GraphQLClient, BillCategory, BillType, BillStatus

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

    @pytest.mark.skipif(not GRAPHQL_AUTH, reason='requires authorization')
    def test_exec_create_bill(self):
        client = GraphQLClient()
        bill = client.exec_create_bill(
            id_='test',
            bill_title='test',
            bill_category=BillCategory.KAKUHOU,
            bill_number=1,
            bill_type=BillType.NEW,
            bill_status=BillStatus.ACCEPTED)
        LOGGER.warning(bill)
        assert bill

    def test_show_all_ops(self):
        LOGGER.warning(GraphQLClient._build_all_bills_operation())
        LOGGER.warning(GraphQLClient._build_create_bill_operation(
            id_='test',
            bill_title='test',
            bill_category=BillCategory.KAKUHOU,
            bill_number=1,
            bill_type=BillType.NEW,
            bill_status=BillStatus.ACCEPTED)
        )
