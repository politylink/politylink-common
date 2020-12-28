from typing import List


class AbstractFinder:
    search_fields = []

    def find(self, text) -> list:
        NotImplemented

    def find_one(self, text):
        objects = self.find(text)
        if len(objects) == 1:
            return objects[0]
        else:
            raise ValueError(f'{self.__class__.__name__} found {len(objects)} results that match with {text}:{objects}')

    @classmethod
    def match(cls, obj, text) -> bool:
        for field in cls.search_fields:
            if hasattr(obj, field):
                for field_text in extract_texts(getattr(obj, field)):
                    if field_text and (text in field_text or field_text in text):
                        return True


def extract_texts(value) -> List[str]:
    """
    recursively extract texts
    """

    texts = []
    if isinstance(value, str):
        texts.append(value)
    elif isinstance(value, list):
        for e in value:
            texts += extract_texts(e)
    return texts
