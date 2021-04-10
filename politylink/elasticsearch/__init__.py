from politylink.utils import get_env_or_default

ELASTICSEARCH_URL = get_env_or_default('ELASTICSEARCH_URL', 'http://localhost:9200')
