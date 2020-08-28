import os
from redis import Redis

R = Redis(host='localhost', port=6379, db=0, decode_responses=True)

app_env = os.environ.get("APP_ENV")
APP_ENV = app_env if app_env else "development"

TEMPLATES = {}

flask_options = { 'static_folder': 'public', 'static_url_path': '' }
