from os import path

import nltk
import pke
from politylink.graphql.client import GraphQLClient
from spacy.lang.ja import stop_words


class KeyPhraseExtractor:

    def __init__(self):
        # load stop words
        p = path.join(path.dirname(__file__), 'stopwords_minutes.txt')
        stopwords_minutes = self.load_stopwords(p)

        p = path.join(path.dirname(__file__), 'stopwords_slothlib.txt')
        stopwords_sloth = self.load_stopwords(p)

        stopwords_members = self.get_member_names()

        # set stop words
        pke.base.lang_stopwords['ja_ginza'] = 'japanese'
        stopwords = list(stop_words.STOP_WORDS | stopwords_minutes | stopwords_sloth | stopwords_members)
        nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
        nltk.corpus.stopwords.words = lambda lang: stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_org(
            lang)

    def load_stopwords(self, path):
        with open(path, mode='r') as f:
            stopwords = set(f.read().splitlines())
        return stopwords

    def get_member_names(self):
        client = GraphQLClient()
        names = ['first_name', 'first_name_hira', 'last_name', 'last_name_hira']
        members = client.get_all_members(fields=names)
        stopwords = []
        for name in names:
            stopwords.extend([m[name] for m in members])
        return set(stopwords)

    def get_key_phrase(self, text, n=3):
        """
        Get key phrases from text
        Up to n key phrases will be returned
        :param text: text
        :param n: maximum number of returned key phrases
        :return: list of key phrases
        """

        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=text, language='ja_ginza', normalization=None)
        extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
        extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)
        key_phrase = extractor.get_n_best(n)
        key_phrase = [k[0] for k in key_phrase]

        return key_phrase
