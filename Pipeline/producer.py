import time
import const
from DatabaseHandler import DatabaseHandler
from Kafka.KafkaConnector import KafkaConnector


class ProducerHandler:
    def __init__(self):
        self.kafka_producer = KafkaConnector().getProducer()
        self.db_handler = DatabaseHandler(const.ALL_CRIME_DBNAME)

    def read_entry(self):
        columns = self.db_handler.get_column_names(const.ALL_CRIME_TABLE)
        is_entry = True
        self.db_handler.cursor.execute(self.db_handler.query)
        while is_entry:
            row = self.db_handler.cursor.fetchone()
            if row:
                # entry = dict(zip((column[0] for column in self.db_handler.cursor.description), row))
                entry = dict(zip((column for column in columns), row))
                self.kafka_producer.produce(KafkaConnector().kafka_topic, value=str(entry))
                self.kafka_producer.flush()
                time.sleep(5)
            else:
                is_entry = False


if __name__ == '__main__':
    producer = ProducerHandler()
    producer.read_entry()
    producer.db_handler.close_connection()
