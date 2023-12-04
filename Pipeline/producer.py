import psycopg2
import time

from confluent_kafka import Producer
import os
from dotenv import load_dotenv

#
#
# connection = psycopg2.connect(
#     host=os.getenv('CRIMESLA_DB_HOST'),
#     database=os.getenv('CRIMESLA_DB_DATABASE'),
#     user=os.getenv('CRIMESLA_DB_USER'),
#     password=os.getenv('CRIMESLA_DB_PASSWORD'),
#     port=os.getenv('CRIMESLA_DB_PORT')
# )
from DatabaseHandler import DatabaseHandler
load_dotenv()

db_handler = DatabaseHandler('CRIMESLA')

kafka_params = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'client.id': os.getenv('KAFKA_CLIENT_ID'),
}

kafka_producer = Producer(kafka_params)

query = "SELECT * FROM allcrimedata;"
db_handler.cursor.execute(query)
kafka_topic = 'crimes_topic'


def read_entry():
    is_entry = True
    while is_entry:
        row = db_handler.cursor.fetchone()
        if row:
            entry = dict(zip((column[0] for column in db_handler.cursor.description), row))
            kafka_producer.produce(kafka_topic, value=str(entry))
            kafka_producer.flush()
            time.sleep(5)
        else:
            is_entry = False


if __name__ == '__main__':
    read_entry()
    db_handler.close_connection()
