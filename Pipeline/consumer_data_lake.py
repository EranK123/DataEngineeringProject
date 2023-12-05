import ast
import re

from confluent_kafka import Consumer, KafkaError
import os
from dotenv import load_dotenv
from uploader import upload_to_crimes_db

load_dotenv()

kafka_params = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest',
}

kafka_consumer = Consumer(kafka_params)
kafka_topic = 'crimes_topic'
kafka_consumer.subscribe([kafka_topic])



def replace_quotes(match):
    return match.group(0).replace("'", '"')


pattern = r"(?<!\w)'(.*?)'"


def consume_and_upload():
    try:
        while True:
            msg = kafka_consumer.poll(timeout=1000)
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            ## need here to send the undecoded message to the data lake
            decoded_message_str = msg.value().decode('utf-8')
            decoded_message_str = re.sub(pattern, replace_quotes, decoded_message_str)
            entry = ast.literal_eval(decoded_message_str)
            upload_to_crimes_db(entry)

    except KeyboardInterrupt:
        pass
    finally:
        kafka_consumer.close()


if __name__ == "__main__":
    consume_and_upload()
