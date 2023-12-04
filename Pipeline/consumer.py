import ast
from confluent_kafka import Consumer, KafkaError
import os
from dotenv import load_dotenv

load_dotenv()
from uploader import upload_to_crimes_db  # Import your uploader module

kafka_params = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest',
}

kafka_consumer = Consumer(kafka_params)
kafka_topic = 'crimes_topic'

kafka_consumer.subscribe([kafka_topic])


def consume_and_upload():
    try:
        while True:
            msg = kafka_consumer.poll(timeout=1000)  # Adjust timeout as needed

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print("Received Message:", msg.value())
            decoded_message_str = msg.value().decode('utf-8')
            decoded_message_str = decoded_message_str.replace("'", "\"")
            print(decoded_message_str)
            entry = ast.literal_eval(decoded_message_str)
            upload_to_crimes_db(entry)

    except KeyboardInterrupt:
        pass
    finally:
        kafka_consumer.close()


if __name__ == "__main__":
    consume_and_upload()
