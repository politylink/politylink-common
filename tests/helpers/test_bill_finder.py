from politylink.graphql.schema import Bill
from politylink.helpers import BillFinder


class TestBillFinder:
    def test_find(self):
        bills = [
            Bill({'id': 'Bill:0', 'name': '法律案A'}),
            Bill({'id': 'Bill:1', 'name': '法律案B'}),
            Bill({'id': 'Bill:2', 'name': '法律案A'})
        ]
        bill_finder = BillFinder(bills)

        assert len(bill_finder.find('法律案A')) == 2
        assert bill_finder.find('法律案A')[0].id == 'Bill:0'
        assert bill_finder.find('法律案A')[1].id == 'Bill:2'

        assert len(bill_finder.find('法律案B')) == 1
        assert bill_finder.find('法律案B')[0].id == 'Bill:1'

        assert len(bill_finder.find('法律案C')) == 0
