from sgqlc.operation import Operation

from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import Query, _MinutesFilter, _Neo4jDateTimeInput


class MinutesFinder:
    """
    GraphQL based Minutes finder
    """

    def __init__(self, **kwargs):
        self.client = GraphQLClient(**kwargs)

    def find(self, text, dt=None):
        op = Operation(Query)
        minutes_filter = _MinutesFilter(None)
        minutes_filter.name_contains = text
        if dt:
            minutes_filter.start_date_time = _Neo4jDateTimeInput(year=dt.year, month=dt.month, day=dt.day)
        op.minutes(filter=minutes_filter)

        data = self.client.endpoint(op)
        GraphQLClient.validate_response_or_raise(data)
        minutes = (op + data).minutes
        return minutes
