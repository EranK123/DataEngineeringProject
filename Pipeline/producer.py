import psycopg2
import time

from confluent_kafka import Producer
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv('CRIMESLA_DB_HOST'),
    database=os.getenv('CRIMESLA_DB_DATABASE'),
    user=os.getenv('CRIMESLA_DB_USER'),
    password=os.getenv('CRIMESLA_DB_PASSWORD'),
    port=os.getenv('CRIMESLA_DB_PORT')
)

kafka_params = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'client.id': os.getenv('KAFKA_CLIENT_ID'),
}

kafka_producer = Producer(kafka_params)

cursor = connection.cursor()
query = "SELECT * FROM allcrimedata;"
cursor.execute(query)
kafka_topic = 'crimes_topic'


def read_entry():
    is_entry = True
    while is_entry:
        row = cursor.fetchone()
        if row:
            entry = dict(zip((column[0] for column in cursor.description), row))
            kafka_producer.produce(kafka_topic, value=str(entry))
            kafka_producer.flush()
            time.sleep(1)
        else:
            is_entry = False


read_entry()
cursor.close()
connection.close()
