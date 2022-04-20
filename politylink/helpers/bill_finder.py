from enum import Enum

from politylink.graphql.client import GraphQLClient
from politylink.helpers.abstract_finder import AbstractFinder, is_text_match
from politylink.helpers.diet_finder import DietFinder
from politylink.utils.bill import extract_bill_number_or_none, extract_bill_category_or_none


class DietRelation(Enum):
    SUBMITTED = 1
    BELONGED = 2


class BillFinder(AbstractFinder):
    """
    Cache based Bill finder
    """

    def __init__(self, bills=None, search_fields=None, **kwargs):
        self.search_fields = search_fields or ['name', 'bill_number', 'category', 'belonged_to_diets']
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient(**kwargs)
            self.bills = client.get_all_bills(['id'] + self.search_fields)
        self.diet_finder = DietFinder()

    def find(self, text, exact_match=False, diet_number=None, diet_relation=None, category=None, date=None):
        # prioritize BilNumber when available
        maybe_bill_number = extract_bill_number_or_none(text)
        if maybe_bill_number:
            text = maybe_bill_number

        # set category from text
        maybe_category = extract_bill_category_or_none(text)
        if maybe_category:
            category = category or maybe_category

        # set diet params from date
        if date:
            diets = self.diet_finder.find(date)
            if len(diets) == 1:
                diet_number = diet_number or diets[0].number
                diet_relation = diet_relation or DietRelation.BELONGED

        return list(filter(
            lambda x: is_text_match(x, self.search_fields, text, exact_match) and
                      is_diet_match(x, diet_number, diet_relation) and
                      is_category_match(x, category),
            self.bills
        ))


def is_diet_match(bill, number=None, relation=None):
    if number is None:
        return True
    relation = relation or DietRelation.SUBMITTED
    if relation == DietRelation.SUBMITTED:
        if hasattr(bill, 'bill_number'):
            return f'第{number}回国会' in bill.bill_number
    elif relation == DietRelation.BELONGED:
        if hasattr(bill, 'belonged_to_diets'):
            for diet in bill.belonged_to_diets:
                if diet.number == number:
                    return True
    return False


def is_category_match(bill, category=None):
    if category is None:
        return True
    if hasattr(bill, 'category'):
        return bill.category == category
    return False
