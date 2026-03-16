from confluent_kafka import Consumer, KafkaError
from shard.logger import log_event
from shard.validation import validate_message

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
                        continue
                    elif msg.error():
                        log_event(level='ERROR', message='Connection to Kafka failed')
                        break

                log_event(level='INFO', message='Received message from Kafka')

                try:
                    data = msg.value()
                    # is_valid = validate_message(data)
                    # if is_valid:
                    #     callback(data)
                    callback(data)
                except:
                    log_event('ERROR', 'not invalid')
                    continue

        finally:
            self.consumer.close()
