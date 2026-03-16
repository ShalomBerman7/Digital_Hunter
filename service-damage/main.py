from shard.kafka_consumer import KafkaConsumer
from shard.logger import log_event

topic = 'damage'
group_id = 'service-damage'
consumer = KafkaConsumer(topic, group_id)


def main(data):
    try:
        print(data)

    except Exception as e:
        log_event('error', e)


if __name__ == '__main__':
    consumer.listen(callback=main)
