from sgqlc.operation import Operation

from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import Query, _MinutesFilter, _Neo4jDateTimeInput


class MinutesFinder:
    def __init__(self):
        self.client = GraphQLClient()

    def find(self, text, year, month, day):
        op = Operation(Query)
        minutes_filter = _MinutesFilter(None)
        minutes_filter.name_contains = text
        minutes_filter.start_date_time = _Neo4jDateTimeInput(year=year, month=month, day=day)
        minutes = op.minutes(filter=minutes_filter)
        minutes.id()
        minutes.name()

        data = self.client.endpoint(op)
        GraphQLClient.validate_response_or_raise(data)
        minutes = (op + data).minutes
        return minutes
