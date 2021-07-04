from politylink.graphql.schema import BillActionType, BillCategory
from politylink.utils.bill import extract_bill_number_or_none, extract_bill_category_or_none, extract_bill_action_types


def test_extract_bill_number_or_none():
    assert extract_bill_number_or_none('地方税法等の一部を改正する法律案（204国会閣9）') == '第204回国会閣法第9号'
    assert extract_bill_number_or_none('第204回国会閣法第9号') == '第204回国会閣法第9号'
    assert extract_bill_number_or_none('第204回国会閣法第9号', short=True) == '204-閣-9'
    assert extract_bill_number_or_none('第二〇四回国会閣法第9号') == '第204回国会閣法第9号'
    assert extract_bill_number_or_none('200衆1') == '第200回国会衆法第1号'
    assert extract_bill_number_or_none('200-衆-1') == '第200回国会衆法第1号'
    assert extract_bill_number_or_none('二〇〇衆一') == '第200回国会衆法第1号'
    assert extract_bill_number_or_none('地方税法等の一部を改正する法律案') is None


def test_extract_bill_category_or_none():
    assert extract_bill_category_or_none('デジタル庁設置法案（内閣提出）') == BillCategory.KAKUHOU
    assert extract_bill_number_or_none('デジタル庁設置法案') is None


def test_extract_bill_action_types():
    assert extract_bill_action_types('これより質疑に入ります。') == [BillActionType.QUESTION]
    assert extract_bill_action_types('本案の趣旨の説明につきましては、これを省略します') == []
