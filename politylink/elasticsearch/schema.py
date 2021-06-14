from enum import Enum

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


class IndexedEnum(Enum):
    def __init__(self, index, *args, **kwargs):
        self.index = index

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

    def __init__(self, index, label):
        super().__init__(index)
        self.label = label

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

    def __init__(self, index, label):
        super().__init__(index)
        self.label = label

    @staticmethod
    def from_gql(bill: Bill):
        for bill_category in BillCategory:
            if bill.category == bill_category.name:
                return bill_category
        raise ValueError(f'bill does not have valid category: {bill.category}')
