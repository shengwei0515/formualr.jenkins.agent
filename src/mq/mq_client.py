import pika

class MQClient:
    
    def __init__(self, host, port, user, password):
        auth = pika.PlainCredentials(user, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=auth, heartbeat=5))
        self.channel = connection.channel()

    def publish_message_to_queue(self, queue_name, msg):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_publish(exchange='',
                                   routing_key=queue_name,
                                   body=msg)

    def consume_on_queue(self, queue_name, callback):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_consume(on_message_callback=callback,
                                   queue=queue_name,
                                   auto_ack=True)
