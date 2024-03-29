import pke
from spacy.lang.ja import stop_words

from politylink.graphql.client import GraphQLClient
from politylink.nlp.utils import load_stopwords, STOPWORDS_SLOTHLIB_PATH, STOPWORDS_MINUTES_PATH


class KeyPhraseExtractor:
    """
    https://zenn.dev/knok/articles/098b265fb2b779
    """

    TEXT_LENGTH_LIMIT = 2000

    def __init__(self):
        # load stop words
        stopwords = set()
        stopwords.update(load_stopwords(STOPWORDS_SLOTHLIB_PATH))
        stopwords.update(load_stopwords(STOPWORDS_MINUTES_PATH))
        stopwords.update(self.get_member_names())
        stopwords.update(stop_words.STOP_WORDS)
        stopwords = list(stopwords)

        # set stop words
        pke.base.stopwords['ja'] = stopwords

    def get_member_names(self):
        client = GraphQLClient()
        fields = ['first_name', 'first_name_hira', 'last_name', 'last_name_hira']
        members = client.get_all_members(fields=fields)
        member_names = [m[f] for f in fields for m in members]
        return member_names

    def extract(self, text, n=3):
        """
        Get key phrases from text
        Up to n key phrases will be returned
        :param text: text
        :param n: maximum number of returned key phrases
        :return: list of key phrases
        """

        # trim text to avoid tokenization error
        if len(text) > self.TEXT_LENGTH_LIMIT:
            text = text[:self.TEXT_LENGTH_LIMIT]

        extractor = pke.unsupervised.MultipartiteRank()  # POL-257: need to init every time
        extractor.load_document(input=text, language='ja', normalization=None)
        extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
        extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)
        key_phrases = extractor.get_n_best(n)
        key_phrases = [k[0] for k in key_phrases]

        return key_phrases
