from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder, is_text_match


class MemberFinder(AbstractFinder):
    """
    Cache based Member finder
    """

    def __init__(self, members=None, search_fields=None, **kwargs):
        self.search_fields = search_fields or ['name', 'name_hira']
        if members:
            self.members = members
        else:
            client = GraphQLClient(**kwargs)
            self.members = client.get_all_members(['id'] + self.search_fields)

    def find(self, text, exact_match=False):
        return list(filter(lambda x: is_text_match(x, self.search_fields, text, exact_match), self.members))
