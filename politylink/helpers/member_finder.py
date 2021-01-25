from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class MemberFinder(AbstractFinder):
    """
    Cache based Member finder
    """

    def __init__(self, members=None, search_fields=None, **kwargs):
        super().__init__(search_fields or ['name', 'name_hira'])
        if members:
            self.members = members
        else:
            client = GraphQLClient(**kwargs)
            self.members = client.get_all_members(['id'] + self.search_fields)

    def find(self, text, exact_match=False, *args, **kwargs):
        return list(filter(lambda x: self.is_text_match(x, text, exact_match), self.members))
