from politylink.graphql.client import GraphQLClient


class BillFinder:
    """
    Cache based Bill finder
    """

    def __init__(self, bills=None, **kwargs):
        if bills:
            self.bills = bills
        else:
            client = GraphQLClient(**kwargs)
            self.bills = client.get_all_bills(['id', 'name', 'bill_number'])

    def find(self, text):
        return list(filter(lambda x: self.match(x, text), self.bills))

    def find_one(self, text):
        bills = self.find(text)
        if len(bills) == 1:
            return bills[0]
        else:
            raise ValueError(f'found {len(bills)} bills that match with {text}:{bills}')

    @staticmethod
    def match(bill, text):
        fields = ['name', 'bill_number']
        for field in fields:
            if hasattr(bill, field) and getattr(bill, field):
                field_text = getattr(bill, field)
                if text in field_text or field_text in text:
                    return True
        return False
