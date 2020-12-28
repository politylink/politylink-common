from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class CommitteeFinder(AbstractFinder):
    """
    Cache based Committee finder
    """

    search_fields = ['name', 'aliases']

    def __init__(self, committees=None, **kwargs):
        if committees:
            self.committees = committees
        else:
            client = GraphQLClient(**kwargs)
            self.committees = client.get_all_committees(['id'] + self.search_fields)

    def find(self, text):
        return list(filter(lambda x: self.match(x, text), self.committees))
