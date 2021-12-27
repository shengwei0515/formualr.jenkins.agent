import os 
import urllib.parse

MQ_HOST =  'jenkins-agent-mq' if os.environ.get("MQ_HOST") == None else os.environ.get("MQ_HOST")
MQ_PORT = '5672' if os.environ.get("MQ_PORT") == None else os.environ.get("MQ_PORT")
MQ_USER = 'small_seal' if os.environ.get("MQ_USER") == None else os.environ.get("MQ_USER")
MQ_PASSWORD = 'password' if os.environ.get("MQ_PASSWORD") == None else os.environ.get("MQ_PASSWORD")
MQ_QUEUE_NAME = "Formular"

API_HOST = '0.0.0.0'
API_PORT = '4000'

# FORMULAR_ENDPOINT = 'https://127.0.0.1:5001' if os.environ.get("FORMULAR_ENDPOINT") == None else os.environ.get("FORMULAR_ENDPOINT")
# FORMULAR_API_ENV_BUILD_INFO = urllib.parse.urljoin(FORMULAR_ENDPOINT, '/api/EnvBuildInfo')