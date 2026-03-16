from confluent_kafka import Consumer, KafkaError
from shard.logger import log_event


conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'service-a',
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

topics = ['intel', 'attack', 'damage']


def get_from_kafka():
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(1.0)
            if msg is None: continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    #loger
                    continue
                elif msg.error():
                    log_event(level='ERROR', message='Connection to Kafka failed')
                    break
            log_event(level='INFO', message='Received message from Kafka')
            print(msg)

    finally:
        consumer.close()

get_from_kafka()