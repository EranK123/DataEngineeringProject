import pandas as pd
from confluent_kafka import Consumer, KafkaError
import os
from dotenv import load_dotenv
from deltalake import write_deltalake, DeltaTable


class KafkaConsumerHandler:
    def __init__(self, bootstrap_servers, group_id, auto_offset_reset, topic, delta_table_path):
        kafka_params = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': auto_offset_reset,
        }

        self.kafka_consumer = Consumer(kafka_params)
        self.kafka_topic = topic
        self.kafka_consumer.subscribe([self.kafka_topic])
        self.delta_table_path = delta_table_path

    def send_to_delta_lake(self, df):
        write_deltalake(self.delta_table_path, df, mode='append')

    def consume_and_send_to_delta_lake(self):
        while True:
            msg = self.kafka_consumer.poll(timeout=1000)
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            raw_message = msg.value().decode('utf-8')
            df = pd.DataFrame([raw_message])
            self.send_to_delta_lake(df)

        self.kafka_consumer.close()


if __name__ == "__main__":
    load_dotenv()
    delta_table_path = os.getenv('DELTA_TABLE_PATH')
    consumer = KafkaConsumerHandler(os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
                                    'my_group',
                                    'earliest',
                                    'crimes_topic',
                                    delta_table_path)
    consumer.consume_and_send_to_delta_lake()
