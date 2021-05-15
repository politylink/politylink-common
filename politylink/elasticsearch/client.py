from enum import Enum

import math
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search

from politylink.elasticsearch import ELASTICSEARCH_URL
from politylink.elasticsearch.schema import AbstractText, to_cls


class OpType(str, Enum):
    INDEX = 'index'  # create or overwrite
    UPDATE = 'update'  # NotFoundError or update
    MERGE = 'merge'  # create or update (round-trip)


class ElasticsearchException(Exception):
    pass


class ElasticsearchClient:
    """
    Elasticsearch client for politylink endpoint
    """

    def __init__(self, url=ELASTICSEARCH_URL):
        self.client = Elasticsearch(url)

    def index(self, obj, op_type=OpType.INDEX):
        """
        create or update a document
        """

        assert isinstance(obj, AbstractText)
        try:
            if op_type == OpType.INDEX:
                return self.client.index(index=obj.index, id=obj.id, body=obj.__dict__)
            elif op_type == OpType.UPDATE:
                return self.client.update(index=obj.index, id=obj.id, body={'doc': obj.__dict__})
            elif op_type == OpType.MERGE:
                if self.exists(obj.id):
                    self.index(obj, op_type=OpType.UPDATE)
                else:
                    self.index(obj, op_type=OpType.INDEX)
            else:
                raise ElasticsearchException(f'unknown index operation type: {op_type}')

        except Exception as e:
            raise ElasticsearchException(f'failed to index {obj}') from e

    def bulk_index(self, objects, op_type=OpType.INDEX):
        def actions():
            for obj in objects:
                assert isinstance(obj, AbstractText)
                if op_type == OpType.INDEX:
                    yield {'_index': obj.index, '_id': obj.id, '_source': obj.__dict__, '_op_type': op_type.value}
                elif op_type == OpType.UPDATE:
                    yield {'_index': obj.index, '_id': obj.id, 'doc': obj.__dict__, '_op_type': op_type.value}
                else:
                    raise ElasticsearchException(f'unknown index operation type: {op_type}')

        try:
            return helpers.bulk(client=self.client, actions=actions())
        except Exception as e:
            raise ElasticsearchException(f'failed to bulk index') from e

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

    def exists(self, id_):
        try:
            cls = to_cls(id_)
            return self.client.exists(index=cls.index, id=id_)
        except Exception as e:
            raise ElasticsearchException(f'failed to check existence of {id_}') from e

    def search(self, cls: AbstractText, query: str = None, start_date_str: str = None, end_date_str: str = None):
        s = Search(using=self.client, index=cls.index)
        if query:
            s = s.query('multi_match', query=query, fields=cls.get_all_fields())
        if start_date_str:
            s = s.filter('range', **{cls.Field.DATE: {'gte': start_date_str}})
        if end_date_str:
            s = s.filter('range', **{cls.Field.DATE: {'lt': end_date_str}})
        try:
            res = s.execute()
            return list(map(lambda hit: cls(hit['_source']), res['hits']['hits']))
        except Exception as e:
            raise ElasticsearchException(f'failed to search {cls.__class__.__name__} for {s.to_dict()}') from e

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
