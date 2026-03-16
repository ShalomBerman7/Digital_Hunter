from shard.kafka_consumer import KafkaConsumer
from shard.logger import log_event

topic = 'attack'
group_id = 'service-attack'
consumer = KafkaConsumer(topic, group_id)


def main(data):
    try:
        print(data)

    except Exception as e:
        log_event('error', e)


if __name__ == '__main__':
    consumer.listen(callback=main)
