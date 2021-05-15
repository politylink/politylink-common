from enum import Enum


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
        FIRST_SUBMITTED_DIET = 'submitted_diet'
        SUBMITTED_DIETS = 'submitted_diets'


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
