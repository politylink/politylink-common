from os import path

import nltk
import pke
from spacy.lang.ja import stop_words


def get_key_phrase(text, n=3):
    """
    Get key phrases from text
    Up to n key phrases will be returned
    :param text: text
    :param n: maximum number of returned key phrases
    :return: list of key phrases
    """

    # load stop words for minutes
    p = path.join(path.dirname(__file__), 'stopwords.txt')
    with open(p, mode='r') as f:
        stopwords_minutes = set(f.read().splitlines())

    # set stop words
    pke.base.lang_stopwords['ja_ginza'] = 'japanese'
    stopwords = list(stop_words.STOP_WORDS | stopwords_minutes)
    nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
    nltk.corpus.stopwords.words = lambda lang: stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_org(
        lang)

    # extract key phrases
    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(input=text, language='ja_ginza', normalization=None)
    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
    extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)
    key_phrase = extractor.get_n_best(n)
    key_phrase = [k[0] for k in key_phrase]

    return key_phrase
