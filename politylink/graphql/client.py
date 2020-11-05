from functools import partial

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _NewsFilter, _Neo4jDateTimeInput

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

    def get(self, id_, fields=None):
        """
        General method to get single GraphQL object by id
        """

        op = self.build_get_operation(id_, fields)
        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        method_name = id_.split(':')[0].lower()
        data = getattr(op + res, method_name)
        if len(data) == 0:
            raise GraphQLException(f'{id_} does not exist')
        elif len(data) == 1:
            return data[0]
        else:
            raise GraphQLException(f'multiple {id_} exist')

    def merge(self, obj):
        """
        General method to merge GraphQL object
        :param obj: GraphQL object
        :return: json data
        """

        op = self.build_merge_operation(obj)
        return self.exec(op)

    def delete(self, id_):
        """
        General method to delete single GraphQL object by id
        """

        op = self.build_delete_operation(id_)
        return self.exec(op)

    def link(self, from_id, to_id):
        """
        General method to link GraphQL objects by id
        :param from_id: politylink id
        :param to_id: politylink id
        :return: json data
        """

        op = self.build_link_operation(from_id, to_id)
        return self.exec(op)

    def unlink(self, from_id, to_id):
        """
        General method to unlink GraphQL objects by id
        :param from_id: politylink id
        :param to_id: politylink id
        :return: json data
        """

        op = self.build_link_operation(from_id, to_id, remove=True)
        return self.exec(op)

    def bulk_merge(self, objects):
        """
        General method to bulk merge GraphQL objects
        requests will be send in batch to avoid Payload Too Large exception
        :param objects: list of GraphQL objects
        :return: json data of the last request
        """

        op_builder_list = map(lambda x: partial(self.build_merge_operation, obj=x), objects)
        return self.bulk_mutation(op_builder_list)

    def bulk_delete(self, ids):
        """
        General method to bulk delete GraphQL objects by id
        requests will be send in batch to avoid Payload Too Large exception
        :param ids: list of politylink ids
        :return: json data of the last request
        """

        op_builder_list = map(lambda x: partial(self.build_delete_operation, id_=x), ids)
        return self.bulk_mutation(op_builder_list)

    def bulk_link(self, from_ids, to_ids):
        """
        General method to bulk link GraphQL objects by id
        requests will be send in batch to avoid Payload Too Large exception
        :param from_ids: list of politylink ids
        :param to_ids: list of politylink ids
        :return: json data of the last request
        """

        op_builder_list = map(lambda x, y: partial(self.build_link_operation, from_id=x, to_id=y), from_ids, to_ids)
        return self.bulk_mutation(op_builder_list)

    def bulk_unlink(self, from_ids, to_ids):
        """
        General method to bulk unlink GraphQL objects by id
        requests will be send in batch to avoid Payload Too Large exception
        :param from_ids: list of politylink ids
        :param to_ids: list of politylink ids
        :return: json data of the last request
        """

        op_builder_list = map(lambda x, y: partial(self.build_link_operation, from_id=x, to_id=y, remove=True),
                              from_ids, to_ids)
        return self.bulk_mutation(op_builder_list)

    def bulk_mutation(self, op_builder_list):
        ret = None
        op = Operation(Mutation)
        for op_builder in op_builder_list:
            op = op_builder(op=op)
            if len(op) >= MAX_BATCH_SIZE:
                ret = self.exec(op)
                op = Operation(Mutation)
        if len(op):
            ret = self.exec(op)
        return ret

    def get_all_bills(self, fields=None):
        """
        Special method to get all Bills
        :return: list of Bills
        """

        if fields is None:
            fields = ['id', 'name', 'bill_number']
        op = self.build_get_all_operation('bill', fields)
        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return (op + res).bill

    def get_all_committees(self, fields=None):
        """
        Special method to get all Committees
        :return: list of Committees
        """

        if fields is None:
            fields = ['id', 'name']
        op = self.build_get_all_operation('committee', fields)
        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return (op + res).committee

    def get_all_minutes(self, fields=None):
        """
        Special method to get all Minutes
        :return: list of Minutes
        """

        if fields is None:
            fields = ['id', 'name', 'start_date_time']
        op = self.build_get_all_operation('minutes', fields)
        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return (op + res).minutes

    def get_all_news(self, fields=None, start_date=None, end_date=None):
        """
        Special method to get all News
        :return: list of News
        """

        if fields is None:
            fields = ['id', 'title', 'published_at', 'url']
        op = self.build_get_all_news_operation(fields, start_date, end_date)
        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return (op + res).news

    @staticmethod
    def validate_response_or_raise(res):
        if 'errors' in res:
            raise GraphQLException(res['errors'])

    @staticmethod
    def build_merge_operation(obj, op=None):
        param = GraphQLClient.build_merge_param(obj)
        if op is None:
            op = Operation(Mutation)
        else:
            param['__alias__'] = f'op{len(op)}'

        method_name = 'merge_{}'.format(obj.id.split(':')[0].lower())
        try:
            res = getattr(op, method_name)(**param)
        except AttributeError:
            raise GraphQLException(f'unknown id type : {id_}')
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
    def build_get_operation(id_, fields=None):
        op = Operation(Query)
        method_name = id_.split(':')[0].lower()
        try:
            obj = getattr(op, method_name)(filter=GraphQLClient.build_filter(id_))
        except AttributeError:
            raise GraphQLException(f'unknown id type : {id_}')
        if fields:
            for field in fields:
                getattr(obj, field)()
        return op

    @staticmethod
    def build_delete_operation(id_, op=None):
        if op is None:
            op = Operation(Mutation)
            maybe_alias = None
        else:
            maybe_alias = f'op{len(op)}'

        method_name = 'delete_{}'.format(id_.split(':')[0].lower())
        try:
            res = getattr(op, method_name)(id=id_, __alias__=maybe_alias)
        except AttributeError:
            raise GraphQLException(f'unknown id type : {id_}')
        res.id()
        return op

    @staticmethod
    def build_link_operation(from_id, to_id, remove=False, op=None):
        if op is None:
            op = Operation(Mutation)
            maybe_alias = None
        else:
            maybe_alias = f'op{len(op)}'

        method_name = 'remove_' if remove else 'merge_'
        if from_id.startswith('Url') and to_id.startswith('Bill'):
            method_name += 'url_referred_bills'
        elif from_id.startswith('Url') and to_id.startswith('Minutes'):
            method_name += 'url_referred_minutes'
        elif from_id.startswith('News') and to_id.startswith('Bill'):
            method_name += 'news_referred_bills'
        elif from_id.startswith('News') and to_id.startswith('Minutes'):
            method_name += 'news_referred_minutes'
        elif from_id.startswith('Speech') and to_id.startswith('Minutes'):
            method_name += 'speech_belonged_to_minutes'
        elif from_id.startswith('Minutes') and to_id.startswith('Bill'):
            method_name += 'minutes_discussed_bills'
        elif from_id.startswith('Minutes') and to_id.startswith('Committee'):
            method_name += 'minutes_belonged_to_committee'
        elif from_id.startswith('Bill') and to_id.startswith('Timeline'):
            method_name += 'timeline_bills'
        elif from_id.startswith('Minutes') and to_id.startswith('Timeline'):
            method_name += 'timeline_minutes'
        elif from_id.startswith('News') and to_id.startswith('Timeline'):
            method_name += 'timeline_news'
        else:
            raise GraphQLException(f'unknown id types to link: from={from_id} to={to_id}')

        res = getattr(op, method_name)(
            from_=GraphQLClient.build_input(from_id),
            to=GraphQLClient.build_input(to_id),
            __alias__=maybe_alias
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def build_input(id_: str):
        # noinspection PyUnresolvedReferences
        from politylink.graphql.schema import _BillInput, _CommitteeInput, _MinutesInput, _SpeechInput, \
            _UrlInput, _NewsInput, _TimelineInput

        class_name = '_{}Input'.format(id_.split(':')[0])
        try:
            return locals()[class_name]({'id': id_})
        except KeyError:
            raise GraphQLException(f'unknown id type to build GraphQL input: {id_}')

    @staticmethod
    def build_filter(id_: str):
        # noinspection PyUnresolvedReferences
        from politylink.graphql.schema import _BillFilter, _CommitteeFilter, _MinutesFilter, _SpeechFilter, \
            _UrlFilter, _NewsFilter, _TimelineFilter

        class_name = '_{}Filter'.format(id_.split(':')[0])
        try:
            return locals()[class_name]({'id': id_})
        except KeyError:
            raise GraphQLException(f'unknown id type to build GraphQL filter: {id_}')

    @staticmethod
    def build_get_all_operation(class_name, fields):
        op = Operation(Query)
        ret = getattr(op, class_name)
        for field in fields:
            getattr(ret, field)()
        return op

    @staticmethod
    def build_get_all_news_operation(fields, start_date=None, end_date=None):
        def to_neo4j_datetime(dt):
            return _Neo4jDateTimeInput(year=dt.year, month=dt.month, day=dt.day)

        op = Operation(Query)
        news_filter = _NewsFilter(None)
        if start_date:
            news_filter.published_at_gte = to_neo4j_datetime(start_date)
        if end_date:
            news_filter.published_at_lt = to_neo4j_datetime(end_date)
        news = op.news(filter=news_filter)
        for field in fields:
            getattr(news, field)()
        return op
