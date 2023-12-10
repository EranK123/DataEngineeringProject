import pandas as pd
from confluent_kafka import Consumer, KafkaError
from datalake.DataLake import DataLake

datalake = DataLake()


class DeltaLakeHandler:
    def __init__(self):
        self.kafka_consumer = Consumer(datalake.kafka_conn.kafka_params)
        self.kafka_consumer.subscribe([datalake.kafka_conn.kafka_topic])

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
            datalake.send_to_delta_lake(df)

        self.kafka_consumer.close()


if __name__ == "__main__":
    consumer = DeltaLakeHandler()
    consumer.consume_and_send_to_delta_lake()
