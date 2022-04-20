from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder, is_text_match


class BillFinder(AbstractFinder):
    """
    Cache based Bill finder
    """

    def __init__(self, bills=None, search_fields=None, **kwargs):
        self.search_fields = search_fields or ['name', 'bill_number', 'category']
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient(**kwargs)
            self.bills = client.get_all_bills(['id'] + self.search_fields)

    def find(self, text, exact_match=False, diet_number=None, category=None, *args, **kwargs):
        return list(filter(
            lambda x: is_text_match(x, self.search_fields, text, exact_match) and
                      is_diet_match(x, diet_number) and
                      is_category_match(x, category),
            self.bills
        ))


def is_diet_match(bill, diet_number=None):
    if diet_number is None:
        return True
    if hasattr(bill, 'bill_number'):
        return f'第{diet_number}回国会' in bill.bill_number
    return False


def is_category_match(bill, category=None):
    if category is None:
        return True
    if hasattr(bill, 'category'):
        return bill.category == category
    return False
