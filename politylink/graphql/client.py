from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import GRAPHQL_AUTH, GRAPHQL_URL
from politylink.graphql.schema import *


class GraphQLException(Exception):
    pass


class GraphQLClient:
    def __init__(self):
        self.endpoint = HTTPEndpoint(GRAPHQL_URL, {'Authorization': GRAPHQL_AUTH})

    def all_bills(self):
        op = self._get_all_bills_op()
        data = self.endpoint(op)
        self._validate_or_fail(data)
        bills = (op + data).all_bills
        return bills

    def create_bill(self, id_, bill_title, bill_category, bill_number, bill_type, bill_status):
        op = self._get_create_bill_op(id_, bill_title, bill_category, bill_number, bill_type, bill_status)
        data = self.endpoint(op)
        self._validate_or_fail(data)
        bill = (op + data).create_bill
        return bill

    @staticmethod
    def _validate_or_fail(data):
        if 'errors' in data:
            raise GraphQLException(data['errors'])

    @staticmethod
    def _get_all_bills_op():
        op = Operation(Query)
        bills = op.all_bills()
        bills.id()
        bills.bill_title()
        minutes = bills.discussed_at()
        minutes.id()
        minutes.minutes_number()
        minutes.discussed_bills()
        minutes.discussed_bills().bill_title()
        return op

    @staticmethod
    def _get_create_bill_op(id_, bill_title, bill_category, bill_number, bill_type, bill_status):
        op = Operation(Mutation)
        bill = op.create_bill(
            id=id_,
            bill_title=bill_title,
            bill_category=bill_category,
            bill_number=bill_number,
            bill_type=bill_type,
            bill_status=bill_status
        )
        bill.id()
        bill.bill_title()
        return op
