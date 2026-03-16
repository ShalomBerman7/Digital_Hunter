from confluent_kafka import Consumer, KafkaError
from shard.logger import log_event
import json


class KafkaConsumer:
    def __init__(self, topic, group_id):
        conf = {'bootstrap.servers': 'localhost:9092',
                'group.id': group_id,
                'auto.offset.reset': 'smallest'}

        self.consumer = Consumer(conf)
        self.topics = topic

    def listen(self, callback):
        try:
            self.consumer.subscribe([self.topics])
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None: continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # loger
                        continue
                    elif msg.error():
                        log_event(level='ERROR', message='Connection to Kafka failed')
                        break
                log_event(level='INFO', message='Received message from Kafka')

                data = json.loads(msg.value())
                callback(data)

        finally:
            self.consumer.close()
