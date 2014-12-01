import os
from ast import literal_eval


def env_eval(var):
    try:
        return literal_eval(var)
    except Exception:
        return var


def config_from_environment(env_prefix, env_required=None, **kwargs):
    config = kwargs.copy()
    prefix = '%s_' % env_prefix.upper()
    for env_key, value in os.environ.items():
        env_key = env_key.upper()
        if env_key.startswith(prefix):
            key = env_key[len(prefix):].lower()
            config[key] = env_eval(value)
    if env_required:
        for required in env_required:
            if required not in config:
                raise RequiredException(
                    'You must pass %s or define env var %s%s' % (
                        required, prefix, required.upper())
                )
    return config


class RequiredException(Exception):
    pass