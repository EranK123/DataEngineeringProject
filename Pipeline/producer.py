import time
from confluent_kafka import Producer
from Kafka.KafkaProducer import KafkaProducer

kafka_producer_handler = KafkaProducer()


class ProducerHandler:
    def __init__(self):
        self.kafka_producer = Producer(kafka_producer_handler.kafka_params)

    def read_entry(self):
        is_entry = True
        while is_entry:
            row = kafka_producer_handler.db_handler.cursor.fetchone()
            if row:
                entry = dict(zip((column[0] for column in kafka_producer_handler.db_handler.cursor.description), row))
                self.kafka_producer.produce(kafka_producer_handler.kafka_topic, value=str(entry))
                self.kafka_producer.flush()
                time.sleep(5)
            else:
                is_entry = False


if __name__ == '__main__':
    producer = ProducerHandler()
    producer.read_entry()
    kafka_producer_handler.db_handler.close_connection()
