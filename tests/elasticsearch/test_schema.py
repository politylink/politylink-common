import politylink.graphql.schema
from politylink.elasticsearch.schema import BillStatus, BillCategory, BillText
from politylink.graphql.schema import Bill, _Neo4jDateTime


def test_bill_status():
    assert BillStatus.from_index(0) == BillStatus.SUBMITTED

    bill = Bill(None)
    bill.submitted_date = _Neo4jDateTime({'formatted': '2021-01-01'})
    bill.passed_representatives_committee_date = _Neo4jDateTime({'formatted': '2021-01-02'})
    bill.passed_representatives_date = _Neo4jDateTime({'formatted': '2021-01-02'})
    assert BillStatus.from_gql(bill) == BillStatus.PASSED_REPRESENTATIVES


def test_bill_category():
    assert BillCategory.from_index(0) == BillCategory.KAKUHOU

    bill = Bill(None)
    bill.category = politylink.graphql.schema.BillCategory.KAKUHOU
    assert BillCategory.from_gql(bill) == BillCategory.KAKUHOU


def test_set_field():
    bill_text = BillText()
    bill_text.set(BillText.Field.ID, 'Bill:1')
    assert bill_text.id == 'Bill:1'
