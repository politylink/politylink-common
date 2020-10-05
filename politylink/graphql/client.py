from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _UrlInput, _BillInput, _SpeechInput, _MinutesInput, _CommitteeInput, _NewsInput

MAX_BATCH_SIZE = 100


class GraphQLException(Exception):
    pass


class GraphQLClient:
    """
    GraphQLClient for PolityLink endpoint
    """

    def __init__(self, url=POLITYLINK_URL, auth=POLITYLINK_AUTH):
        self.endpoint = HTTPEndpoint(url, {'Authorization': auth}, timeout=30)

    def exec(self, op):
        """
        General method to execute GraphQL operation (query or mutation)
        :param op: GraphQL operation string
        :return: json data
        """

        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return res['data']

    def merge(self, obj):
        """
        General method to merge GraphQL object
        :param obj: GraphQL object
        :return: json data
        """

        op = self.build_merge_operation(obj)
        return self.exec(op)

    def bulk_merge(self, objects):
        """
        General method to bulk merge GraphQL objects
        requests will be send in batch to avoid Payload Too Large exception
        :param objects: list of GraphQL objects
        :return: json data of the last request
        """

        data = None
        for i in range(0, len(objects), MAX_BATCH_SIZE):
            batch_objects = objects[i:i + MAX_BATCH_SIZE]
            op = Operation(Mutation)
            for obj in batch_objects:
                op = self.build_merge_operation(obj, op)
            data = self.exec(op)
        return data

    def link(self, from_id, to_id):
        """
        General method to link GraphQL objects by id
        :param from_id: politylink id
        :param to_id: politylink id
        :return: json data
        """

        op = self.build_link_operation(from_id, to_id)
        return self.exec(op)

    def bulk_link(self, from_ids, to_ids):
        """
        General method to bulk link GraphQL objects by id
        requests will be send in batch to avoid Payload Too Large exception
        :param from_ids: list of politylink ids
        :param to_ids: list of politylink ids
        :return: json data of the last request
        """

        data = None
        for i in range(0, len(from_ids), MAX_BATCH_SIZE):
            batch_from_ids = from_ids[i:i + MAX_BATCH_SIZE]
            batch_to_ids = to_ids[i:i + MAX_BATCH_SIZE]
            op = Operation(Mutation)
            for from_id, to_id in zip(batch_from_ids, batch_to_ids):
                op = self.build_link_operation(from_id, to_id, op)
            data = self.exec(op)
        return data

    def get_all_bills(self):
        """
        Special method to get all Bills
        :return: list of Bills
        """

        op = self.build_all_bills_operation()
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        bills = (op + data).bill
        return bills

    def get_all_committees(self):
        """
        Special method to get all Committees
        :return: list of Committees
        """

        op = self.build_all_committees_operation()
        data = self.endpoint(op)
        self.validate_response_or_raise(data)
        committees = (op + data).committee
        return committees

    @staticmethod
    def validate_response_or_raise(res):
        if 'errors' in res:
            raise GraphQLException(res['errors'])

    @staticmethod
    def build_all_bills_operation():
        op = Operation(Query)
        bills = op.bill()
        bills.id()
        bills.name()
        bills.bill_number()
        return op

    @staticmethod
    def build_all_committees_operation():
        op = Operation(Query)
        committees = op.committee()
        committees.id()
        committees.name()
        committees.aliases()
        return op

    @staticmethod
    def build_merge_operation(obj, op=None):
        param = GraphQLClient.build_merge_param(obj)
        if op is None:
            op = Operation(Mutation)
        else:
            param['__alias__'] = f'op{len(op)}'
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
    def build_merge_param(obj):
        param = dict()
        for field_name in obj.__field_names__:
            if hasattr(obj, field_name):
                param[field_name] = getattr(obj, field_name)
        return param

    @staticmethod
    def build_link_operation(from_id, to_id, op=None):
        if op is None:
            op = Operation(Mutation)
            maybe_alias = None
        else:
            maybe_alias = f'op{len(op)}'
        if from_id.startswith('Url') and to_id.startswith('Bill'):
            res = op.merge_url_referred_bills(
                from_=_UrlInput({'id': from_id}),
                to=_BillInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('Url') and to_id.startswith('Minutes'):
            res = op.merge_url_referred_minutes(
                from_=_UrlInput({'id': from_id}),
                to=_MinutesInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('News') and to_id.startswith('Bill'):
            res = op.merge_news_referred_bills(
                from_=_NewsInput({'id': from_id}),
                to=_BillInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('News') and to_id.startswith('Minutes'):
            res = op.merge_news_referred_minutes(
                from_=_NewsInput({'id': from_id}),
                to=_MinutesInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('Speech') and to_id.startswith('Minutes'):
            res = op.merge_speech_belonged_to_minutes(
                from_=_SpeechInput({'id': from_id}),
                to=_MinutesInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('Minutes') and to_id.startswith('Bill'):
            res = op.merge_minutes_discussed_bills(
                from_=_MinutesInput({'id': from_id}),
                to=_BillInput({'id': to_id}),
                __alias__=maybe_alias
            )
        elif from_id.startswith('Minutes') and to_id.startswith('Committee'):
            res = op.merge_minutes_belonged_to_committee(
                from_=_MinutesInput({'id': from_id}),
                to=_CommitteeInput({'id': to_id}),
                __alias__=maybe_alias
            )
        else:
            raise GraphQLException(f'unknown id types to link: from={from_id} to={to_id}')
        res.from_.id()
        res.to.id()
        return op
