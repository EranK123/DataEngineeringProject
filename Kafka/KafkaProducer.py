from DatabaseHandler import DatabaseHandler
import const


class KafkaProducer:
    def __init__(self):
        self.db_handler = DatabaseHandler(const.ALL_CRIME_DBNAME)
        self.kafka_params = {
            'bootstrap.servers': const.KAFKA_BOOTSTRAP_SERVERS,
            'client.id': const.KAFKA_CLIENT_ID,
        }
        self.db_handler.cursor.execute(self.db_handler.query)
        self.kafka_topic = const.KAFKA_TOPIC
