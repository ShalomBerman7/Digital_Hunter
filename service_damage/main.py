from shard.kafka_consumer import KafkaConsumer
from shard.logger import log_event
from service_damage.models import create_database, create_table, insert_into


topic = 'damage'
group_id = 'service_damage'
consumer = KafkaConsumer(topic, group_id)


def main(data):
    try:
        create_database()
        create_table()
        insert_into(data['timestamp'], data['signal_id'], data['entity_id'], data['weapon_type'])
        log_event('info', 'inserted item to intel')

    except Exception as e:
        log_event('error', e)


if __name__ == '__main__':
    consumer.listen(callback=main)
