from os import path

import spacy
from spacy.lang.ja import stop_words

nlp = spacy.load('ja_ginza')

WORDCLOUD_POS_TAGS = ['ADJ', 'ADV', 'NOUN', 'PROPN']
STOPWORDS_SLOTHLIB_PATH = path.join(path.dirname(__file__), 'stopwords_slothlib.txt')
STOPWORDS_MINUTES_PATH = path.join(path.dirname(__file__), 'stopwords_minutes.txt')


def filter_by_pos(texts, pos_tags):
    """
    filter text that includes target Part-Of-Speech tags
    https://spacy.io/api/annotation#pos-tagging
    """

    ret = []
    for doc in nlp.pipe(texts):
        for token in doc:
            if token.pos_ in pos_tags:
                ret.append(doc.text)
                break
    return ret


def load_stopwords(file_path):
    with open(file_path, mode='r') as f:
        stopwords = f.read().splitlines()
    return set(stopwords)


STOPWORDS = set()
STOPWORDS.update(load_stopwords(STOPWORDS_SLOTHLIB_PATH))
STOPWORDS.update(stop_words.STOP_WORDS)
