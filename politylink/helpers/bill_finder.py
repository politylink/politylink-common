from collections import defaultdict

from politylink.graphql.client import GraphQLClient


class BillFinder:
    def __init__(self, bills=None):
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient()
            self.bills = client.exec_all_bills()
        self.name2bills = defaultdict(list)
        for bill in self.bills:
            self.name2bills[bill.name].append(bill)

    def find(self, text):
        return self.name2bills[text]
