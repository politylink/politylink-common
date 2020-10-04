from collections import defaultdict

from politylink.graphql.client import GraphQLClient


class BillFinder:
    """
    Cache based Bill finder
    """

    def __init__(self, bills=None):
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient()
            self.bills = client.get_all_bills()
        self.name2bills = defaultdict(list)
        self.number2bill = defaultdict(list)
        for bill in self.bills:
            if hasattr(bill, 'name'):
                self.name2bills[bill.name].append(bill)
            if hasattr(bill, 'bill_number'):
                self.number2bill[bill.bill_number].append(bill)

    def find(self, text):
        return self.name2bills[text] + self.number2bill[text]
