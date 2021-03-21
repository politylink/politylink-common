import spacy

nlp = spacy.load('ja_ginza')

WORDCLOUD_POS_TAGS = ['ADJ', 'ADV', 'NOUN', 'PROPN']


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
