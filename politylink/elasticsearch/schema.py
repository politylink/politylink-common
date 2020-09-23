from enum import Enum


class AbstractText:
    """
    Abstract class to define elasticsearch document schema
    """

    # define index name here
    index = NotImplemented

    # define document schema here
    class Field(str, Enum):
        ID = 'id'  # 'id' is required

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
        return all field names except for 'id'
        """

        fields = []
        for field in cls.Field:
            if field.name != 'ID':
                fields.append(field.value)
        return fields


class NewsText(AbstractText):
    index = 'news'

    class Field(str, Enum):
        ID = 'id'
        TITLE = 'title'
        BODY = 'body'


class BillText(AbstractText):
    index = 'bill'

    class Field(str, Enum):
        ID = 'id'
        TITLE = 'title'
        BODY = 'body'
        SUPPL = 'suppl'
        REASON = 'reason'
