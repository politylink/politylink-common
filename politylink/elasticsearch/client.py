from urllib.parse import urlparse

from elasticsearch import Elasticsearch

from politylink.elasticsearch.schema import NewsText, BillText, AbstractText


class ElasticsearchClientException(Exception):
    pass


class ElasticsearchClient:
    """
    Elasticsearch client for politylink endpoint
    """

    def __init__(self, url='http://localhost:9200'):
        def to_node(url):
            res = urlparse(url)
            return {'host': res.hostname, 'port': res.port}

        self.client = Elasticsearch(hosts=[to_node(url)])

    def index(self, obj):
        """
        create or update a document
        """

        assert isinstance(obj, AbstractText)
        try:
            return self.client.index(index=obj.index, id=obj.id, body=obj.__dict__)
        except Exception as e:
            raise ElasticsearchClientException(f'failed to index {obj}') from e

    def get(self, id_):
        """
        get a document by politylink id (ref idgen)
        """

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
            raise ElasticsearchClientException(f'failed to search NewsText for {query_doc}') from e
