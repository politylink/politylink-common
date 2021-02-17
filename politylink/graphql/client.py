from functools import partial

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from politylink.graphql import POLITYLINK_AUTH, POLITYLINK_URL
from politylink.graphql.schema import *
from politylink.graphql.schema import _NewsFilter, _Neo4jDateTimeInput, _ActivityFilter


class GraphQLException(Exception):
    pass


class GraphQLClient:
    """
    GraphQLClient for PolityLink endpoint
    """

    def __init__(self, url=POLITYLINK_URL, auth=POLITYLINK_AUTH, batch_size=100):
        self.endpoint = HTTPEndpoint(url, {'Authorization': auth}, timeout=30)
        self.batch_size = batch_size

    def exec(self, op):
        """
        General method to execute GraphQL operation (query or mutation)
        :param op: GraphQL operation string
        :return: json data
        """

        res = self.endpoint(op)
        self.validate_response_or_raise(res)
        return res['data']

    def get(self, id_, fields=None, depth=2):
        """
        General method to get single GraphQL object by id
        """

        op = self.build_get_operation(id_, fields)
        res = self.endpoint(op.__to_graphql__(auto_select_depth=depth))
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
            if len(op) >= self.batch_size:
                ret = self.exec(op)
                op = Operation(Mutation)
        if len(op):
            ret = self.exec(op)
        return ret

    def get_all_bills(self, fields=None, filter_=None, depth=1):
        """
        Special method to get all Bills
        :return: list of Bill
        """

        if fields is None:
            fields = ['id', 'name', 'bill_number']
        return self.get_all_objects('bill', fields, filter_, depth)

    def get_all_committees(self, fields=None, filter_=None, depth=1):
        """
        Special method to get all Committees
        :return: list of Committee
        """

        if fields is None:
            fields = ['id', 'name']
        return self.get_all_objects('committee', fields, filter_, depth)

    def get_all_minutes(self, fields=None, filter_=None, depth=1):
        """
        Special method to get all Minutes
        :return: list of Minutes
        """

        if fields is None:
            fields = ['id', 'name', 'start_date_time']
        return self.get_all_objects('minutes', fields, filter_, depth)

    def get_all_members(self, fields=None, filter_=None, depth=1):
        """
        Special method to get all Members
        :return: list of Member
        """

        if fields is None:
            fields = ['id', 'name']
        return self.get_all_objects('member', fields, filter_, depth)

    def get_all_diets(self, fields=None, filter_=None, depth=1):
        """
        Special method to get all Diets
        :return: list of Diet
        """

        if fields is None:
            fields = ['id', 'number']
        return self.get_all_objects('diet', fields, filter_, depth)

    def get_all_news(self, fields=None, filter_=None, depth=1, start_date=None, end_date=None):
        """
        Special method to get all News
        :return: list of News
        """

        def to_neo4j_datetime(dt):
            return _Neo4jDateTimeInput(year=dt.year, month=dt.month, day=dt.day)

        if fields is None:
            fields = ['id', 'title', 'published_at', 'url']
        if filter_ is None:
            filter_ = _NewsFilter(None)
        if start_date:
            filter_.published_at_gte = to_neo4j_datetime(start_date)
        if end_date:
            filter_.published_at_lt = to_neo4j_datetime(end_date)
        return self.get_all_objects('news', fields, filter_, depth)

    def get_all_activities(self, fields=None, filter_=None, depth=1, member_id=None, bill_id=None, minutes_id=None):
        """
        Special method to get all Activities
        :return: list of Activity
        """

        if fields is None:
            fields = ['id', 'datetime', 'member_id', 'bill_id', 'minutes_id']
        if filter_ is None:
            filter_ = _ActivityFilter(None)
        if member_id:
            filter_.member_id = member_id
        if bill_id:
            filter_.bill_id = bill_id
        if minutes_id:
            filter_.minutes_id = minutes_id
        return self.get_all_objects('activity', fields, filter_, depth)

    def get_all_objects(self, class_name, fields=None, filter_=None, depth=1):
        op = self.build_get_all_operation(class_name, fields, filter_)
        res = self.endpoint(op.__to_graphql__(auto_select_depth=depth))
        self.validate_response_or_raise(res)
        return getattr(op + res, class_name)

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
            raise GraphQLException(f'unknown id type : {obj.id}')
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

        method_name = GraphQLClient.build_link_method_name(from_id, to_id, remove)
        res = getattr(op, method_name)(
            from_=GraphQLClient.build_input(from_id),
            to=GraphQLClient.build_input(to_id),
            __alias__=maybe_alias
        )
        res.from_.id()
        res.to.id()
        return op

    @staticmethod
    def build_link_method_name(from_id, to_id, remove=False):
        from_id_type = from_id.split(':')[0]
        to_id_type = to_id.split(':')[0]
        key = (from_id_type, to_id_type)

        if key not in _link_method_name_map:
            raise GraphQLException(f'unknown id types to link: from={from_id} to={to_id}')

        method_prefix = 'remove' if remove else 'merge'
        method_body = _link_method_name_map[key]
        return f'{method_prefix}_{method_body}'

    @staticmethod
    def build_input(id_: str):
        # noinspection PyUnresolvedReferences
        from politylink.graphql.schema import _BillInput, _CommitteeInput, _MinutesInput, _SpeechInput, \
            _UrlInput, _NewsInput, _TimelineInput, _MemberInput, _DietInput, _ActivityInput

        class_name = '_{}Input'.format(id_.split(':')[0])
        try:
            return locals()[class_name]({'id': id_})
        except KeyError:
            raise GraphQLException(f'unknown id type to build GraphQL input: {id_}')

    @staticmethod
    def build_filter(id_: str):
        # noinspection PyUnresolvedReferences
        from politylink.graphql.schema import _BillFilter, _CommitteeFilter, _MinutesFilter, _SpeechFilter, \
            _UrlFilter, _NewsFilter, _TimelineFilter, _MemberFilter, _DietFilter, _ActivityFilter

        class_name = '_{}Filter'.format(id_.split(':')[0])
        try:
            return locals()[class_name]({'id': id_})
        except KeyError:
            raise GraphQLException(f'unknown id type to build GraphQL filter: {id_}')

    @staticmethod
    def build_get_all_operation(class_name, fields=None, filter_=None):
        op = Operation(Query)
        ret = getattr(op, class_name)(filter=filter_)
        if fields is not None:
            for field in fields:
                getattr(ret, field)()
        return op


# key1: from id type, key2: to id type, value: link method name
# we may automatically generate this map from schema.py
_link_method_name_map = {
    ('Url', 'Bill'): 'url_referred_bills',
    ('Url', 'Law'): 'url_referred_laws',
    ('Url', 'Member'): 'url_referred_members',
    ('Url', 'Minutes'): 'url_referred_minutes',
    ('Url', 'Activity'): 'url_referred_activities',
    ('News', 'Bill'): 'news_referred_bills',
    ('News', 'Law'): 'news_referred_laws',
    ('News', 'Member'): 'news_referred_members',
    ('News', 'Minutes'): 'news_referred_minutes',
    ('News', 'Timeline'): 'timeline_news',
    ('Activity', 'Member'): 'activity_member',
    ('Activity', 'Minutes'): 'activity_minutes',
    ('Activity', 'Bill'): 'activity_bill',
    ('Speech', 'Minutes'): 'speech_belonged_to_minutes',
    ('Minutes', 'Bill'): 'minutes_discussed_bills',
    ('Minutes', 'Law'): 'minutes_discussed_laws',
    ('Minutes', 'Committee'): 'minutes_belonged_to_committee',
    ('Minutes', 'Timeline'): 'timeline_minutes',
    ('Minutes', 'Diet'): 'minutes_belonged_to_diet',
    ('Bill', 'Committee'): 'bill_belonged_to_committees',
    ('Bill', 'Timeline'): 'timeline_bills',
    ('Bill', 'Diet'): 'bill_belonged_to_diets',
    ('Member', 'Bill'): 'member_submitted_bills',
    ('Member', 'Diet'): 'member_attended_diets',
    ('Member', 'Speech'): 'member_delivered_speeches',
    ('Member', 'Minutes'): 'member_attended_minutes'
}
