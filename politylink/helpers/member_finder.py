from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class MemberFinder(AbstractFinder):
    """
    Cache based Member finder
    """

    search_fields = ['name', 'name_hira']

    def __init__(self, members=None, **kwargs):
        if members:
            self.members = members
        else:
            client = GraphQLClient(**kwargs)
            self.members = client.get_all_members(['id'] + self.search_fields)

    def find(self, text):
        return list(filter(lambda x: self.match(x, text), self.members))
