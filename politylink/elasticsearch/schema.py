from enum import Enum

import politylink.graphql.schema
from politylink.graphql.schema import Bill


def to_cls(id_):
    """
    map Politylink ID to ElasticSearch schema class
    """

    if id_.startswith('News'):
        return NewsText
    elif id_.startswith('Bill'):
        return BillText
    elif id_.startswith('Minutes'):
        return MinutesText
    elif id_.startswith('Speech'):
        return SpeechText
    elif id_.startswith('Member'):
        return MemberText
    else:
        raise ValueError(f'unknown id type: {id_}')


class AbstractText:
    """
    Abstract class to define elasticsearch document schema
    """

    # define index name here
    index = NotImplemented

    # define document schema here
    class Field(str, Enum):
        ID = 'id'  # 'id' is required
        DATE = 'date'  # 2020-01-01

    def __init__(self, dct=None):
        if dct:
            for field in self.Field:
                key = field.value
                if key in dct:
                    setattr(self, key, dct[key])

    def set(self, field: Field, value):
        setattr(self, field.value, value)

    def get(self, field: Field):
        getattr(self, field.value)

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.__dict__}>'

    @classmethod
    def get_all_fields(cls):
        """
        return all field names except for ID and DATE
        """

        fields = []
        for field in cls.Field:
            if field.name not in {cls.Field.ID.name, cls.Field.DATE.name}:
                fields.append(field.value)
        return fields


class NewsText(AbstractText):
    index = 'news'

    class Field(str, Enum):
        ID = 'id'
        TITLE = 'title'
        BODY = 'body'
        DATE = 'date'


class BillText(AbstractText):
    index = 'bill'

    class Field(str, Enum):
        ID = 'id'
        BILL_NUMBER = 'bill_number'
        TITLE = 'title'
        BODY = 'body'
        SUPPLEMENT = 'supplement'
        REASON = 'reason'
        ALIASES = 'aliases'
        TAGS = 'tags'
        CATEGORY = 'category'
        STATUS = 'status'
        SUBMITTED_DATE = 'submitted_date'
        LAST_UPDATED_DATE = 'last_updated_date'
        GROUPS = 'groups'
        MINISTRIES = 'ministries'
        SUBMITTED_DIET = 'submitted_diet'
        BELONGED_TO_DIETS = 'belonged_to_diets'
        SUBMITTED_GROUPS = 'submitted_groups'
        SUPPORTED_GROUPS = 'supported_groups'
        OPPOSED_GROUPS = 'opposed_groups'


class MinutesText(AbstractText):
    index = 'minutes'

    class Field(str, Enum):
        ID = 'id'
        TITLE = 'title'
        BODY = 'body'
        DATE = 'date'


class SpeechText(AbstractText):
    index = 'speech'

    class Field(str, Enum):
        ID = 'id'
        TITLE = 'title'
        SPEAKER = 'speaker'
        BODY = 'body'
        DATE = 'date'


class MemberText(AbstractText):
    index = 'member'

    class Field(str, Enum):
        ID = 'id'
        NAME = 'name'
        NAME_HIRA = 'name_hira'
        DESCRIPTION = 'description'
        GROUP = 'group'
        LAST_UPDATED_DATE = 'last_updated_date'
        HOUSE = 'house'


class IndexedEnum(Enum):
    def __init__(self, index, label):
        self.index = index
        self.label = label

    @classmethod
    def from_index(cls, index: int):
        for e in cls:
            if e.index == index:
                return e
        raise ValueError(f'index not found: {index}')


class BillStatus(IndexedEnum):
    SUBMITTED = (0, '提出')
    PASSED_REPRESENTATIVES_COMMITTEE = (1, '衆委可決')
    PASSED_REPRESENTATIVES = (2, '衆可決')
    PASSED_COUNCILORS_COMMITTEE = (3, '参委可決')
    PASSED_COUNCILORS = (4, '参可決')
    PROCLAIMED = (5, '公布')

    @staticmethod
    def from_gql(bill: Bill):
        max_date, max_bill_status = '', None
        for bill_status in BillStatus:
            gql_date_field = bill_status.name.lower() + '_date'
            if hasattr(bill, gql_date_field):
                date = getattr(bill, gql_date_field).formatted
                if date and date >= max_date:  # >= to prioritize later
                    max_date = date
                    max_bill_status = bill_status
        if max_bill_status is None:
            raise ValueError(f'bill does not have valid date: {bill}')
        return max_bill_status


class BillCategory(IndexedEnum):
    KAKUHOU = (0, '閣法')
    SHUHOU = (1, '衆法')
    SANHOU = (2, '参法')

    @staticmethod
    def from_gql(bill: Bill):
        for bill_category in BillCategory:
            if bill.category == bill_category.name:
                return bill_category
        raise ValueError(f'bill does not have valid category: {bill.category}')


class ParliamentaryGroup(IndexedEnum):
    JIMIN = (0, '自民')
    RIKKEN = (1, '立憲')
    KOMEI = (2, '公明')
    KYOSAN = (3, '共産')
    ISHIN = (4, '維新')
    KOKUMIN = (5, '国民')

    @staticmethod
    def from_gql(gql_group: politylink.graphql.schema.ParliamentaryGroup):
        for es_group in ParliamentaryGroup:
            if gql_group == es_group.name:
                return es_group
        raise ValueError(f'failed to map ParliamentaryGroup: {gql_group}')


class House(IndexedEnum):
    REPRESENTATIVES = (0, '衆議院')
    COUNCILORS = (1, '参議院')

    @staticmethod
    def from_gql(gql_house: politylink.graphql.schema.House):
        for es_house in House:
            if gql_house == es_house.name:
                return es_house
        raise ValueError(f'failed to map House: {gql_house}')
