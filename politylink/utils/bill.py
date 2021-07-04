import re
from logging import getLogger
from typing import List

from politylink.graphql.schema import BillActionType, BillCategory
from politylink.utils import contains_word, replace_kansuji_to_number

LOGGER = getLogger(__name__)


def extract_bill_number_or_none(text, short=False):
    pattern = r'第?([0-9]+)回?-?(国会)?(閣|衆|参)法?-?第?([0-9]+)号?'
    match = re.search(pattern, replace_kansuji_to_number(text))
    if not match:
        return None
    template = '{}-{}-{}' if short else '第{}回国会{}法第{}号'
    return template.format(match.group(1), match.group(3), match.group(4))


def extract_bill_category_or_none(text) -> BillCategory:
    if contains_word(text, ['内閣提出', '閣法']):
        return BillCategory.KAKUHOU
    elif contains_word(text, ['衆議院提出', '衆法']):
        return BillCategory.SHUHOU
    elif contains_word(text, ['参議院提出', '参法']):
        return BillCategory.SANHOU
    return None


def extract_bill_action_types(speech) -> List[BillActionType]:
    action_lst = []
    if contains_word(speech, ['説明'], ['省略', '終わり', '既に聴取']):
        if contains_word(speech, ['修正案']):
            action_lst.append(BillActionType.AMENDMENT_EXPLANATION)
        elif contains_word(speech, ['附帯決議']):
            action_lst.append(BillActionType.SUPPLEMENTARY_EXPLANATION)
        elif contains_word(speech, ['趣旨の説明', '趣旨説明']):
            action_lst.append(BillActionType.BILL_EXPLANATION)
    if contains_word(speech, ['質疑']):
        action_lst.append(BillActionType.QUESTION)
    if contains_word(speech, ['討論']):
        action_lst.append(BillActionType.DEBATE)
    if contains_word(speech, ['採決']):
        action_lst.append(BillActionType.VOTE)
    if contains_word(speech, ['委員長の報告']):
        action_lst.append(BillActionType.REPORT)
    return action_lst
