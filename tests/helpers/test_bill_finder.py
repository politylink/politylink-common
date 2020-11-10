import pytest

from politylink.graphql.schema import Bill
from politylink.helpers import BillFinder


class TestBillFinder:
    def test_find(self):
        bills = [
            Bill({'id': 'Bill:0', 'name': '法律案A'}),
            Bill({'id': 'Bill:1', 'name': '法律案B'}),
            Bill({'id': 'Bill:2', 'name': '法律案A', 'billNumber': '第1号'})
        ]
        bill_finder = BillFinder(bills)

        assert len(bill_finder.find('法律案A')) == 2
        assert bill_finder.find('法律案A')[0].id == 'Bill:0'
        assert bill_finder.find('法律案A')[1].id == 'Bill:2'
        with pytest.raises(ValueError):
            bill_finder.find_one('法律案A')

        assert len(bill_finder.find('法律案B')) == 1
        assert bill_finder.find('法律案B')[0].id == 'Bill:1'
        assert bill_finder.find_one('法律案B').id == 'Bill:1'

        assert len(bill_finder.find('法律案C')) == 0
        with pytest.raises(ValueError):
            bill_finder.find_one('法律案C')

        assert len(bill_finder.find('第1号')) == 1
        assert bill_finder.find('第1号')[0].id == 'Bill:2'

        assert len(bill_finder.find('第2号')) == 0
        assert len(bill_finder.find('法律案')) == 3
        assert len(bill_finder.find('法律案A(成立)')) == 2
