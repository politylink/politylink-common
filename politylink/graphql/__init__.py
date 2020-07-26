from politylink.utils import get_env_or_default

POLITYLINK_URL = get_env_or_default('POLITYLINK_URL', 'http://www.politylink.jp:4000/')
POLITYLINK_AUTH = get_env_or_default('POLITYLINK_AUTH', '')
