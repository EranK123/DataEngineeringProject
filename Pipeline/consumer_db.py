import ast
import re
from confluent_kafka import Consumer, KafkaError
import os
from dotenv import load_dotenv
from uploader import upload_to_crimes_db

load_dotenv()


class KafkaConsumerHandler:
    def __init__(self, bootstrap_servers, group_id, auto_offset_reset, topic):
        kafka_params = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': auto_offset_reset,
        }

        self.kafka_consumer = Consumer(kafka_params)
        self.kafka_topic = topic
        self.kafka_consumer.subscribe([self.kafka_topic])

    def replace_quotes(self, match):
        return match.group(0).replace("'", '"')

    def consume_and_upload(self):
        try:
            while True:
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

        except KeyboardInterrupt:
            pass
        finally:
            self.kafka_consumer.close()


if __name__ == "__main__":
    consumer = KafkaConsumerHandler(os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
                                    'my_group',
                                    'earliest',
                                    'crimes_topic')
    consumer.consume_and_upload()
