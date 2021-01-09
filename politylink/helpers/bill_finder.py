from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class BillFinder(AbstractFinder):
    """
    Cache based Bill finder
    """

    def __init__(self, bills=None, search_fields=None, **kwargs):
        super().__init__(search_fields or ['name', 'bill_number'])
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient(**kwargs)
            self.bills = client.get_all_bills(['id'] + self.search_fields)

    def find(self, text, exact_match=False):
        return list(filter(lambda x: self.match(x, text, exact_match), self.bills))
