from deltalake import write_deltalake
from Kafka.KafkaConnector import KafkaConnector
import const


class DataLake:
    def __init__(self):
        self.kafka_conn = KafkaConnector()
        self.delta_table_path = const.DELTA_TABLE_PATH

    def send_to_delta_lake(self, df):
        write_deltalake(self.delta_table_path, df, mode='append')
