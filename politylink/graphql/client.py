from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _UrlInput, _BillInput, _SpeechInput, _MinutesInput, _CommitteeInput, _NewsInput


class GraphQLException(Exception):
    pass


class GraphQLClient:
    """
    GraphQLClient for PolityLink endpoint
    """

    def __init__(self, url=POLITYLINK_URL, auth=POLITYLINK_AUTH):
        self.endpoint = HTTPEndpoint(url, {'Authorization': auth}, timeout=3)

    def exec(self, query_str):
        """
        General method to execute GraphQL query or mutation
        :param query_str: GraphQL query/mutation string
        :return: json response
        """

        data = self.endpoint(query_str)
        self.validate_response_or_raise(data)
        return data

    def merge(self, obj):
        """
        General method to merge GraphQL object
        :param obj: GraphQL object
        :return: json response
        """

        op = self.build_merge_operation(obj)
        return self.exec(op)

    def exec_all_bills(self):
        op = self._build_all_bills_operation()
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        bills = (op + data).bill
        return bills

    def exec_all_committees(self):
        op = self._build_all_committees_operation()
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        committees = (op + data).committee
        return committees

    def exec_merge_url_referred_bills(self, url_id, bill_id):
        op = self._build_merge_url_referred_bills(url_id, bill_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_url_referred_bills
        return res

    def exec_merge_url_referred_minutes(self, url_id, minutes_id):
        op = self._build_merge_url_referred_minutes(url_id, minutes_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_url_referred_minutes
        return res

    def exec_merge_news_referred_bills(self, news_id, bill_id):
        op = self._build_merge_news_referred_bills(news_id, bill_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_news_referred_bills
        return res

    def exec_merge_news_referred_minutes(self, news_id, minutes_id):
        op = self._build_merge_news_referred_minutes(news_id, minutes_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_news_referred_minutes
        return res

    def exec_merge_speech_belonged_to_minutes(self, speech_id, minutes_id):
        op = self._build_merge_speech_belonged_to_minutes(speech_id, minutes_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_speech_belonged_to_minutes
        return res

    def exec_merge_minutes_discussed_bills(self, minutes_id, bill_id):
        op = self._build_merge_minutes_discussed_bills(minutes_id, bill_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_minutes_discussed_bills
        return res

    def exec_merge_minutes_belonged_to_committee(self, minutes_id, committee_id):
        op = self._build_merge_minutes_belonged_to_committee(minutes_id, committee_id)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        res = (op + data).merge_minutes_belonged_to_committee
        return res

    @staticmethod
    def validate_response_or_raise(data):
        if 'errors' in data:
            raise GraphQLException(data['errors'])

    @staticmethod
    def _build_all_bills_operation():
        op = Operation(Query)
        bills = op.bill()
        bills.id()
        bills.name()
        bills.bill_number()
        return op

    @staticmethod
    def _build_all_committees_operation():
        op = Operation(Query)
        committees = op.committee()
        committees.id()
        committees.name()
        committees.aliases()
        return op

    @staticmethod
    def build_merge_operation(obj):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_param(obj)
        if isinstance(obj, Bill):
            res = op.merge_bill(**param)
        elif isinstance(obj, Url):
            res = op.merge_url(**param)
        elif isinstance(obj, News):
            res = op.merge_news(**param)
        elif isinstance(obj, Minutes):
            res = op.merge_minutes(**param)
        elif isinstance(obj, Committee):
            res = op.merge_committee(**param)
        elif isinstance(obj, Speech):
            res = op.merge_speech(**param)
        else:
            raise GraphQLException(f'unknown object type to merge: {type(obj)}')
        res.id()
        return op

    @staticmethod
    def _build_merge_param(obj):
        param = dict()
        for field_name in obj.__field_names__:
            if hasattr(obj, field_name):
                param[field_name] = getattr(obj, field_name)
        return param

    @staticmethod
    def _build_merge_url_referred_bills(url_id, bill_id):
        op = Operation(Mutation)
        res = op.merge_url_referred_bills(
            from_=_UrlInput({'id': url_id}),
            to=_BillInput({'id': bill_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_url_referred_minutes(url_id, minutes_id):
        op = Operation(Mutation)
        res = op.merge_url_referred_minutes(
            from_=_UrlInput({'id': url_id}),
            to=_MinutesInput({'id': minutes_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_news_referred_bills(news_id, bill_id):
        op = Operation(Mutation)
        res = op.merge_news_referred_bills(
            from_=_NewsInput({'id': news_id}),
            to=_BillInput({'id': bill_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_news_referred_minutes(news_id, minutes_id):
        op = Operation(Mutation)
        res = op.merge_news_referred_minutes(
            from_=_NewsInput({'id': news_id}),
            to=_MinutesInput({'id': minutes_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_speech_belonged_to_minutes(speech_id, minutes_id):
        op = Operation(Mutation)
        res = op.merge_speech_belonged_to_minutes(
            from_=_SpeechInput({'id': speech_id}),
            to=_MinutesInput({'id': minutes_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_minutes_discussed_bills(minutes_id, bill_id):
        op = Operation(Mutation)
        res = op.merge_minutes_discussed_bills(
            from_=_MinutesInput({'id': minutes_id}),
            to=_BillInput({'id': bill_id})
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def _build_merge_minutes_belonged_to_committee(minutes_id, committee_id):
        op = Operation(Mutation)
        res = op.merge_minutes_belonged_to_committee(
            from_=_MinutesInput({'id': minutes_id}),
            to=_CommitteeInput({'id': committee_id})
        )
        res.from_.id()
        res.to.id()
        return op
