import const


class KafkaConsumer:
    def __init__(self):
        self.kafka_params = {
            'bootstrap.servers': const.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': const.KAFKA_GROUP,
            'auto.offset.reset': 'earliest',
        }
        self.kafka_topic = 'crimes_topic'
