import psycopg2
import time

from confluent_kafka import Producer

from Pipeline import uploader

db_params = {
    'host': 'localhost',
    'database': 'crimesla',
    'user': 'postgres',
    'password': 'Peach124',
    'port': 5432
}

connection = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password'],
    port=db_params['port']
)

kafka_params = {
    'bootstrap.servers': 'localhost:9092',  # Update with your Kafka bootstrap servers
    'client.id': 'crimes_producer',
}

kafka_producer = Producer(kafka_params)


cursor = connection.cursor()
query = "SELECT * FROM allcrimedata;"
cursor.execute(query)


def read_entry():
    is_entry = True
    while is_entry:
        row = cursor.fetchone()
        if row:
            entry = dict(zip((column[0] for column in cursor.description), row))
            kafka_topic = 'crimes_topic'
            kafka_producer.produce(kafka_topic, value=str(entry))
            # yield entry
            kafka_producer.flush()
            time.sleep(5)
        else:
            is_entry = False


#
# for entry in read_entry():
#     print(entry)


# for entry in read_entry():
#     uploader.upload_to_crimes_db(entry)
cursor.close()
connection.close()
