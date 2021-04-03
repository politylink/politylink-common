from urllib.parse import urlparse

import math
from elasticsearch import Elasticsearch

from politylink.elasticsearch.schema import AbstractText, to_cls


class ElasticsearchException(Exception):
    pass


class ElasticsearchClient:
    """
    Elasticsearch client for politylink endpoint
    """

    def __init__(self, url='http://localhost:9200'):
        self.client = Elasticsearch(url)

    def index(self, obj):
        """
        create or update a document
        """

        assert isinstance(obj, AbstractText)
        try:
            return self.client.index(index=obj.index, id=obj.id, body=obj.__dict__)
        except Exception as e:
            raise ElasticsearchException(f'failed to index {obj}') from e

    def get(self, id_):
        """
        get a document by politylink id (ref idgen)
        """

        try:
            cls = to_cls(id_)
            res = self.client.get(index=cls.index, id=id_)
            return cls(res['_source'])
        except Exception as e:
            raise ElasticsearchException(f'failed to get {id_}') from e

    def search(self, cls, query=None):
        """
        search $cls documents by query
        return all documents when query is empty
        """

        if query:
            query_doc = {'query': {'multi_match': {'query': query, 'fields': cls.get_all_fields()}}}
        else:
            query_doc = {'query': {'match_all': {}}}
        try:
            res = self.client.search(index=cls.index, body=query_doc)
            return list(map(lambda hit: cls(hit['_source']), res['hits']['hits']))
        except Exception as e:
            raise ElasticsearchException(f'failed to search {cls.__class__.__name__} for {query_doc}') from e

    def get_term_statistics(self, id_):
        """
        get term statistics using termvectors API

        :param id_: politylink ID
        :return: dictionary of term to statistics (tf, idf, tfidf)
        """

        try:
            cls = to_cls(id_)
            res = self.client.termvectors(index=cls.index, id=id_, params={'fields': 'body', 'term_statistics': 'true'})
        except Exception as e:
            raise ElasticsearchException(f'failed to get termvectors for {id_}') from e

        term2stats = dict()
        doc_count = res['term_vectors']['body']['field_statistics']['doc_count']
        for term, stats_raw in res['term_vectors']['body']['terms'].items():
            stats = dict()
            stats['tf'] = stats_raw['term_freq']
            stats['idf'] = math.log(doc_count / stats_raw['doc_freq'])
            stats['tfidf'] = stats['tf'] * stats['idf']
            term2stats[term] = stats
        return term2stats
