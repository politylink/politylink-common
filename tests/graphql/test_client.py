from logging import getLogger

import pytest

from politylink.graphql.client import GraphQLClient, BillCategory, BillType, BillStatus

LOGGER = getLogger(__name__)


class TestGraphQLClient:
    def test_all_bills(self):
        client = GraphQLClient()
        bills = client.all_bills()
        LOGGER.warning(bills)
        assert len(bills) > 0

    @pytest.mark.skip(reason='requires authorization')
    def test_create_bill(self):
        client = GraphQLClient()
        bill = client.create_bill(
            id_='test',
            bill_title='test',
            bill_category=BillCategory.KAKUHOU,
            bill_number=1,
            bill_type=BillType.NEW,
            bill_status=BillStatus.ACCEPTED)
        LOGGER.warning(bill)
        assert bill

    def test_show_all_ops(self):
        LOGGER.warning(GraphQLClient._get_all_bills_op())
        LOGGER.warning(GraphQLClient._get_create_bill_op(
            id_='test',
            bill_title='test',
            bill_category=BillCategory.KAKUHOU,
            bill_number=1,
            bill_type=BillType.NEW,
            bill_status=BillStatus.ACCEPTED)
        )
