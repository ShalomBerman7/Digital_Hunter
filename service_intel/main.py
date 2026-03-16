from shard.kafka_consumer import KafkaConsumer
from shard.logger import log_event
from service_intel.models import create_database, create_table, insert_into

topic = 'intel'
group_id = 'service_intel'
consumer = KafkaConsumer(topic, group_id)


def main(data):
    try:
        create_database()
        create_table()
        insert_into(data['timestamp'], data['signal_id'], data['entity_id'], data['reported_lat'], data['reported_lon'], data['signal_type'], data['priority_level'])
        log_event('info', 'inserted item to intel')

    except:
        log_event('error', 'not invalid')


if __name__ == '__main__':
    consumer.listen(callback=main)
