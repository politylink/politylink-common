from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder, is_text_match


class CommitteeFinder(AbstractFinder):
    """
    Cache based Committee finder
    """

    def __init__(self, committees=None, search_fields=None, **kwargs):
        self.search_fields = search_fields or ['name', 'aliases']
        if committees:
            self.committees = committees
        else:
            client = GraphQLClient(**kwargs)
            self.committees = client.get_all_committees(['id'] + self.search_fields)

    def find(self, text, exact_match=False, *args, **kwargs):
        return list(filter(lambda x: is_text_match(x, self.search_fields, text, exact_match), self.committees))
