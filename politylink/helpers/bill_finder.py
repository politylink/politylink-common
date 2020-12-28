from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class BillFinder(AbstractFinder):
    """
    Cache based Bill finder
    """

    search_fields = ['name', 'bill_number']

    def __init__(self, bills=None, **kwargs):
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient(**kwargs)
            self.bills = client.get_all_bills(['id'] + self.search_fields)

    def find(self, text):
        return list(filter(lambda x: self.match(x, text), self.bills))
