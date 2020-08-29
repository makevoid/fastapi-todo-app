import os
from redis import Redis

app_env = os.environ.get("APP_ENV")
APP_ENV = app_env if app_env else "development"

redis_host = "redis" if app_env == "production" else 'localhost'
R = Redis(host=redis_host, port=6379, db=0, decode_responses=True)


TEMPLATES = {}
