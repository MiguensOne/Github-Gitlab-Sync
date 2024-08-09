import os

GITLAB_URL = os.environ.get('GITLAB_URL', None); assert GITLAB_URL is not None 
PRIVATE_TOKEN = os.environ.get('GITLAB_TOKEN', None); assert PRIVATE_TOKEN is not None
PROJECT_ID = os.environ.get('PROJECT_ID', None); assert PROJECT_ID is not None
POLL_INTERVAL = os.environ.get('POLL_INTERVAL', 10)