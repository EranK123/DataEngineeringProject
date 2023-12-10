import ast
import re
from confluent_kafka import Consumer, KafkaError

from Kafka.KafkaConsumer import KafkaConsumer
from uploader import upload_to_crimes_db

kafka_consumer_handler = KafkaConsumer()


class ConsumerHandler:
    def __init__(self):
        self.kafka_consumer = Consumer(kafka_consumer_handler.kafka_params)
        self.kafka_consumer.subscribe([kafka_consumer_handler.kafka_topic])

    def replace_quotes(self, match):
        return match.group(0).replace("'", '"')

    def consume_and_upload(self):
        while True: #for loop on msg
            msg = self.kafka_consumer.poll(timeout=1000)
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            decoded_message_str = msg.value().decode('utf-8')
            decoded_message_str = re.sub(r"(?<!\w)'(.*?)'", self.replace_quotes, decoded_message_str)
            entry = ast.literal_eval(decoded_message_str)
            upload_to_crimes_db(entry)

        self.kafka_consumer.close()


if __name__ == "__main__":
    consumer = ConsumerHandler()
    consumer.consume_and_upload()
