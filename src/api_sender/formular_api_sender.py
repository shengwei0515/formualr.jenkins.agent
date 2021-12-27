import json
import datetime
import pytz
import dataclasses
import requests
import config
from mq.mq_client import MQClient
from formular.models import EnvBuildInfoParameter
from urllib3.exceptions import InsecureRequestWarning



mqclient = MQClient(config.MQ_HOST, config.MQ_PORT, config.MQ_USER, config.MQ_PASSWORD)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def get_msg_from_mq_and_send_api(ch, method, properties, body):
    body = json.loads(body.decode("utf-8"))
    build_info = EnvBuildInfoParameter(**body)
    payload = dataclasses.asdict(build_info)
    timestamp = datetime.datetime.now(tz=pytz.timezone("Asia/Taipei"))
    try:
        r = requests.post(config.FORMULAR_API_ENV_BUILD_INFO, json=payload, verify=False)
        print(f"{timestamp} [Info] Send request with response code: {r.status_code}, payload: {payload}")
    except Exception as e:
        print(f"{timestamp} [Error] send api failed with error: {e}, payload: {payload}")

mqclient.consume_on_queue(config.MQ_QUEUE_NAME, get_msg_from_mq_and_send_api)