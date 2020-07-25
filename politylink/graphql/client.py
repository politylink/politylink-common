from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import GRAPHQL_AUTH, GRAPHQL_URL
from politylink.graphql.schema import *


class GraphQLException(Exception):
    pass


class GraphQLClient:
    """
    GraphQLClient for politylink endpoint
    """

    def __init__(self):
        self.endpoint = HTTPEndpoint(GRAPHQL_URL, {'Authorization': GRAPHQL_AUTH})

    def exec(self, query_str):
        """
        General method to execute GraphQL query or mutation
        :param query_str: GraphQL query/mutation string
        :return: json response
        """

        data = self.endpoint(query_str)
        self._validate_or_raise(data)
        return data

    def exec_all_bills(self):
        """
        Special method to execute allBills query
        :return: list of Bill
        """

        op = self._build_all_bills_operation()
        data = self.endpoint(op)
        self._validate_or_raise(data)
        bills = (op + data).all_bills
        return bills

    def exec_create_bill(self, id_, bill_title, bill_category, bill_number, bill_type, bill_status):
        """
        Special method to execute createBill mutation
        :return: created Bill
        """

        op = self._build_create_bill_operation(id_, bill_title, bill_category, bill_number, bill_type, bill_status)
        data = self.endpoint(op)
        self._validate_or_raise(data)
        bill = (op + data).create_bill
        return bill

    @staticmethod
    def _validate_or_raise(data):
        if 'errors' in data:
            raise GraphQLException(data['errors'])

    @staticmethod
    def _build_all_bills_operation():
        op = Operation(Query)
        bills = op.all_bills()
        bills.id()
        bills.bill_title()
        minutes = bills.discussed_at()
        minutes.id()
        minutes.minutes_number()
        return op

    @staticmethod
    def _build_create_bill_operation(id_, bill_title, bill_category, bill_number, bill_type, bill_status):
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
