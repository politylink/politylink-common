from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder


class DietFinder(AbstractFinder):
    """
    Cache based Diet finder
    """

    def __init__(self, diets=None, **kwargs):
        if diets:
            self.diets = diets
        else:
            client = GraphQLClient(**kwargs)
            self.diets = client.get_all_diets(['id', 'start_date', 'end_date'])

    def find(self, date):
        return list(filter(lambda x: is_date_match(x, date), self.diets))


def is_date_match(diet, date):
    def to_str(dt):
        return f'{dt.year:04}-{dt.month:02}-{dt.day:02}'

    print('eval {} <= {} <= {}'.format(to_str(diet.start_date), to_str(date), to_str(diet.end_date)))
    return to_str(diet.start_date) <= to_str(date) <= to_str(diet.end_date)
