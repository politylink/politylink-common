from enum import Enum
from os import path

import spacy
from spacy.lang.ja import stop_words

nlp = spacy.load('ja_ginza')

WORDCLOUD_POS_TAGS = ['ADJ', 'ADV', 'NOUN', 'PROPN']
STOPWORDS_SLOTHLIB_PATH = path.join(path.dirname(__file__), 'stopwords_slothlib.txt')
STOPWORDS_MINUTES_PATH = path.join(path.dirname(__file__), 'stopwords_minutes.txt')


class MatchMode(str, Enum):
    ANY = 'any'
    ALL = 'all'
    LAST = 'last'


def filter_by_pos(texts, pos_tags, mode=MatchMode.ANY):
    """
    filter text that match with target Part-Of-Speech tags
    https://spacy.io/api/annotation#pos-tagging
    """

    ret = []
    for doc in nlp.pipe(texts):
        if mode == MatchMode.ANY:
            is_match = any([token.pos_ in pos_tags for token in doc])
        elif mode == MatchMode.ALL:
            is_match = all([token.pos_ in pos_tags for token in doc])
        elif mode == MatchMode.LAST:
            is_match = doc[-1].pos_ in pos_tags
        else:
            raise ValueError(f'unknown match mode: {mode}')
        if is_match:
            ret.append(doc.text)
    return ret


def load_stopwords(file_path):
    with open(file_path, mode='r') as f:
        stopwords = f.read().splitlines()
    return set(stopwords)


STOPWORDS = set()
STOPWORDS.update(load_stopwords(STOPWORDS_SLOTHLIB_PATH))
STOPWORDS.update(stop_words.STOP_WORDS)
