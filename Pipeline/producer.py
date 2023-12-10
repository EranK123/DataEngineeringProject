import time
from confluent_kafka import Producer
import const
from DatabaseHandler import DatabaseHandler
from Kafka.KafkaConnector import KafkaConnector

kafka_connector = KafkaConnector()
db_handler = DatabaseHandler(const.ALL_CRIME_DBNAME)
db_handler.cursor.execute(db_handler.query)


class ProducerHandler:
    def __init__(self):
        self.kafka_producer = Producer(kafka_connector.kafka_params)

    def read_entry(self):
        is_entry = True
        while is_entry:
            row = db_handler.cursor.fetchone()
            if row:
                entry = dict(zip((column[0] for column in db_handler.cursor.description), row))
                self.kafka_producer.produce(kafka_connector.kafka_topic, value=str(entry))
                self.kafka_producer.flush()
                time.sleep(5)
            else:
                is_entry = False


if __name__ == '__main__':
    producer = ProducerHandler()
    producer.read_entry()
    db_handler.close_connection()
