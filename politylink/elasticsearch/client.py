from elasticsearch import Elasticsearch

from politylink.elasticsearch.schema import NewsText, BillText


class ElasticsearchClientException(Exception):
    pass


class ElasticsearchClient:
    """
    Elasticsearch client for politylink endpoint
    """

    def __init__(self):
        self.client = Elasticsearch()  # ToDo: use PROD host by default

    def index(self, obj):
        try:
            return self.client.index(index=obj.index, id=obj.id, body=obj.__dict__)
        except Exception as e:
            raise ElasticsearchClientException(f'failed to index {obj}') from e

    def get(self, id_):
        try:
            if id_.startswith('News'):
                cls = NewsText
            elif id_.startswith('Bill'):
                cls = BillText
            res = self.client.get(index=cls.index, id=id_)
            return cls(res['_source'])
        except Exception as e:
            raise ElasticsearchClientException(f'failed to get {id_}') from e

    def search(self, cls, query=None):
        if query:
            query_doc = {'query': {'multi_match': {'query': query, 'fields': cls.get_all_fields()}}}
        else:
            query_doc = {'query': {'match_all': {}}}
        try:
            res = self.client.search(index=cls.index, body=query_doc)
            return list(map(lambda hit: cls(hit['_source']), res['hits']['hits']))
        except Exception as e:
            raise ElasticsearchClientException(f'failed to search NewsText for {query_doc}') from e
