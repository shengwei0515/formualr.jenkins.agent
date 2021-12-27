import json
import dataclasses
import config

from flask import Flask, request
from formular.models import *
from mq.mq_client import MQClient


app = Flask(__name__)

@app.route('/api/Formular/EvnBuildInfo', methods=['POST'])
def get_payload_and_publish_to_mq():
    data = request.json
    formular_model = EnvBuildInfoParameter(**data)
    json_string = json.dumps(dataclasses.asdict(formular_model))
    try:
        mqclient = MQClient(config.MQ_HOST, config.MQ_PORT, config.MQ_USER, config.MQ_PASSWORD)
        mqclient.publish_message_to_queue(config.MQ_QUEUE_NAME, json_string)
        return f"Insert {json_string} to mq success", 200
    except Exception as e:
        return f"Insert {json_string} to mq failed with error {e}", 403

