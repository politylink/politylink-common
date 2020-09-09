from politylink.utils import get_env_or_default

POLITYLINK_URL = get_env_or_default('POLITYLINK_URL', 'https://graphql.politylink.jp')
POLITYLINK_AUTH = get_env_or_default('POLITYLINK_AUTH', '')
