import psycopg2
import time

from confluent_kafka import Producer
import os
from dotenv import load_dotenv

from DatabaseHandler import DatabaseHandler

load_dotenv()


class KafkaProducerHandler:
    def __init__(self, db_name, bootstrap_servers, client_id):
        self.db_handler = DatabaseHandler(db_name)

        # self.kafka_params = {
        #     'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
        #     'client.id': os.getenv('KAFKA_CLIENT_ID'),
        # }
        self.kafka_params = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': client_id,
        }
        self.kafka_producer = Producer(self.kafka_params)

        self.query = "SELECT * FROM allcrimedata;"
        self.db_handler.cursor.execute(self.query)
        self.kafka_topic = 'crimes_topic'

    def read_entry(self):
        is_entry = True
        while is_entry:
            row = self.db_handler.cursor.fetchone()
            if row:
                entry = dict(zip((column[0] for column in self.db_handler.cursor.description), row))
                self.kafka_producer.produce(self.kafka_topic, value=str(entry))
                self.kafka_producer.flush()
                time.sleep(5)
            else:
                is_entry = False



if __name__ == '__main__':
    producer = KafkaProducerHandler('CRIMESLA', os.getenv('KAFKA_BOOTSTRAP_SERVERS'), os.getenv('KAFKA_CLIENT_ID'))
    producer.read_entry()
    producer.db_handler.close_connection()
