from deltalake import write_deltalake

import const


class DataLake:
    def __init__(self):
        self.kafka_params = {
            'bootstrap.servers': const.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': const.KAFKA_GROUP,
            'auto.offset.reset': 'earliest',
        }
        self.kafka_topic = const.KAFKA_TOPIC
        self.delta_table_path = const.DELTA_TABLE_PATH

    def send_to_delta_lake(self, df):
        write_deltalake(self.delta_table_path, df, mode='append')
