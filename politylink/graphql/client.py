from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _UrlInput, _BillInput


class GraphQLException(Exception):
    pass


class GraphQLClient:
    """
    GraphQLClient for politylink endpoint
    """

    def __init__(self):
        self.endpoint = HTTPEndpoint(POLITYLINK_URL, {'Authorization': POLITYLINK_AUTH}, timeout=3)

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
        op = self._build_all_bills_operation()
        data = self.endpoint(op)
        self._validate_or_raise(data)
        bills = (op + data).all_bills
        return bills

    def exec_merge_bill(self, bill):
        op = self._build_merge_bill_operation(bill)
        data = self.endpoint(op)
        self._validate_or_raise(data)
        bill = (op + data).merge_bill
        return bill

    def exec_merge_url(self, url):
        op = self._build_merge_url_operation(url)
        data = self.endpoint(op)
        self._validate_or_raise(data)
        url = (op + data).merge_url
        return url

    def exec_merge_url_referred_bills(self, url_id, bill_id):
        op = self._build_merge_url_referred_bills(url_id, bill_id)
        data = self.endpoint(op)
        self._validate_or_raise(data)
        res = (op + data).merge_url_referred_bills
        return res

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
        minutes = bills.be_discussed_by_minutes()
        minutes.id()
        minutes.minutes_number()
        return op

    @staticmethod
    def _build_merge_bill_operation(bill):
        op = Operation(Mutation)
        param = dict()
        for field in Bill.__field_names__:
            if hasattr(bill, field):
                param[field] = getattr(bill, field)
        merged_bill = op.merge_bill(**param)
        merged_bill.id()
        return op

    @staticmethod
    def _build_merge_url_operation(url):
        op = Operation(Mutation)
        param = dict()
        for field in Url.__field_names__:
            if hasattr(url, field):
                param[field] = getattr(url, field)
        merged_url = op.merge_url(**param)
        merged_url.id()
        return op

    @staticmethod
    def _build_merge_url_referred_bills(url_id, bill_id):
        op = Operation(Mutation)
        _url_input = _UrlInput()
        _url_input.id = url_id
        _bill_input = _BillInput()
        _bill_input.id = bill_id
        res = op.merge_url_referred_bills(from_=_url_input, to=_bill_input)
        res.from_.id()
        res.to.id()
        return op
