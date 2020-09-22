from enum import Enum


class AbstractText:
    index = NotImplemented

    class Field(str, Enum):
        NotImplemented

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
