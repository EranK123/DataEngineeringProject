import const


class KafkaConnector:
    def __init__(self):
        self.kafka_params = {
            'bootstrap.servers': const.KAFKA_BOOTSTRAP_SERVERS,
            'client.id': const.KAFKA_CLIENT_ID,
            'group.id': const.KAFKA_GROUP,
            'auto.offset.reset': 'earliest',
        }
        self.kafka_topic = const.KAFKA_TOPIC
