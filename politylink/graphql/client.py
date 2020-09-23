from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _UrlInput, _BillInput, _SpeechInput, _MinutesInput, _CommitteeInput, _NewsInput


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
        self.validate_response_or_raise(data)
        return data

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

    def exec_merge_bill(self, bill):
        op = self._build_merge_bill_operation(bill)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        bill = (op + data).merge_bill
        return bill

    def exec_merge_url(self, url):
        op = self._build_merge_url_operation(url)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        url = (op + data).merge_url
        return url

    def exec_merge_news(self, news):
        op = self._build_merge_news_operation(news)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        news = (op + data).merge_news
        return news

    def exec_merge_minutes(self, minutes):
        op = self._build_merge_minutes_operation(minutes)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        minutes = (op + data).merge_minutes
        return minutes

    def exec_merge_committee(self, committee):
        op = self._build_merge_committee_operation(committee)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        committee = (op + data).merge_committee
        return committee

    def exec_merge_speech(self, speech):
        op = self._build_merge_speech_operation(speech)
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        speech = (op + data).merge_speech
        return speech

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
    def _build_merge_bill_operation(bill):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(bill, Bill.__field_names__)
        merged_bill = op.merge_bill(**param)
        merged_bill.id()
        return op

    @staticmethod
    def _build_merge_url_operation(url):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(url, Url.__field_names__)
        merged_url = op.merge_url(**param)
        merged_url.id()
        return op

    @staticmethod
    def _build_merge_news_operation(news):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(news, News.__field_names__)
        merged_news = op.merge_news(**param)
        merged_news.id()
        return op

    @staticmethod
    def _build_merge_minutes_operation(minutes):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(minutes, Minutes.__field_names__)
        merged_minutes = op.merge_minutes(**param)
        merged_minutes.id()
        return op

    @staticmethod
    def _build_merge_committee_operation(committee):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(committee, Committee.__field_names__)
        merged_committee = op.merge_committee(**param)
        merged_committee.id()
        return op

    @staticmethod
    def _build_merge_speech_operation(speech):
        op = Operation(Mutation)
        param = GraphQLClient._build_merge_obj_param(speech, Speech.__field_names__)
        merged_speech = op.merge_speech(**param)
        merged_speech.id()
        return op

    @staticmethod
    def _build_merge_obj_param(obj, field_names):
        param = dict()
        for field_name in field_names:
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
