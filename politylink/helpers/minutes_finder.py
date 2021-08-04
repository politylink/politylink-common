from politylink.graphql.client import GraphQLClient
from politylink.graphql.schema import _MinutesFilter, _Neo4jDateTimeInput


class MinutesFinder:
    """
    GraphQL based Minutes finder
    """

    def __init__(self, **kwargs):
        self.client = GraphQLClient(**kwargs)

    def find(self, text, dt=None):
        minutes_filter = _MinutesFilter(None)
        minutes_filter.name_contains = text
        if dt:
            minutes_filter.start_date_time = _Neo4jDateTimeInput(year=dt.year, month=dt.month, day=dt.day)
        return self.client.get_all_minutes(fields=['id', 'name', 'start_date_time'], filter_=minutes_filter)
