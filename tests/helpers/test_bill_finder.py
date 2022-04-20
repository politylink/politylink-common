import pytest

from politylink.graphql.schema import Bill, BillCategory
from politylink.helpers import BillFinder
from politylink.helpers.bill_finder import is_diet_match, DietRelation


class TestBillFinder:
    def test_find(self):
        bills = [
            Bill({'id': 'Bill:0', 'name': '法律案A'}),
            Bill({'id': 'Bill:1', 'name': '法律案B'}),
            Bill({'id': 'Bill:2', 'name': '法律案A', 'billNumber': '第100回国会閣法第1号', 'category': 'KAKUHOU'})
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

        assert len(bill_finder.find('法律案', diet_number=100)) == 1
        assert len(bill_finder.find('法律案', diet_number=101)) == 0

        assert len(bill_finder.find('法律案', category=BillCategory.KAKUHOU)) == 1
        assert len(bill_finder.find('法律案', category=BillCategory.SANHOU)) == 0


def test_is_diet_match():
    bill = Bill({
        'id': 'Bill:0',
        'billNumber': '第200回国会閣法第1号',
        'belongedToDiets': [{'number': 200}, {'number': 201}]
    })

    assert not is_diet_match(bill, 199, DietRelation.SUBMITTED)
    assert is_diet_match(bill, 200, DietRelation.SUBMITTED)
    assert not is_diet_match(bill, 201, DietRelation.SUBMITTED)

    assert not is_diet_match(bill, 199, DietRelation.BELONGED)
    assert is_diet_match(bill, 200, DietRelation.BELONGED)
    assert is_diet_match(bill, 201, DietRelation.BELONGED)
    assert not is_diet_match(bill, 202, DietRelation.BELONGED)
