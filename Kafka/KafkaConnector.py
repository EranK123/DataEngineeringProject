import const
from confluent_kafka import Producer
from confluent_kafka import Consumer
from singelton_decorator import singleton


@singleton
class KafkaConnector:
    def __init__(self):
        self.kafka_params = {
            'bootstrap.servers': const.KAFKA_BOOTSTRAP_SERVERS,
            'client.id': const.KAFKA_CLIENT_ID,
            'group.id': const.KAFKA_GROUP,
            'auto.offset.reset': 'earliest',
        }
        self.kafka_topic = const.KAFKA_TOPIC

    def getProducer(self):
        return Producer(self.kafka_params)

    def getConsumer(self):
        kafka_consumer = Consumer(self.kafka_params)
        kafka_consumer.subscribe([self.kafka_topic])
        return kafka_consumer
