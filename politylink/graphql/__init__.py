import os

GRAPHQL_URL = 'http://www.politylink.jp:4000/'  # ToDo: use local server on local
GRAPHQL_AUTH = os.environ['GRAPHQL_AUTH'] if 'GRAPHQL_AUTH' in os.environ else ''
