import os


def get_env_or_default(key, default):
    return os.environ[key] if key in os.environ else default
