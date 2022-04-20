from typing import List


class AbstractFinder:
    def find(self, *args, **kwargs) -> list:
        NotImplemented

    def find_one(self, *args, **kwargs):
        objects = self.find(*args, **kwargs)
        if len(objects) == 1:
            return objects[0]
        else:
            raise ValueError(
                f'{self.__class__.__name__} found {len(objects)} results: query={kwargs}, results={objects}')


def is_text_match(obj, search_fields, text, exact_match=False) -> bool:
    for field in search_fields:
        if hasattr(obj, field):
            for field_text in extract_texts(getattr(obj, field)):
                if exact_match:
                    if text == field_text:
                        return True
                else:
                    if text in field_text or field_text in text:
                        return True
    return False


def extract_texts(value) -> List[str]:
    """
    recursively extract texts
    """

    texts = []
    if isinstance(value, str) and value:
        texts.append(value)
    elif isinstance(value, list):
        for e in value:
            texts += extract_texts(e)
    return texts
