import threading
from Pipeline.producer import ProducerHandler
from Pipeline.consumer_db import ConsumerHandler


def producer_task():
    producer = ProducerHandler()
    producer.read_entry()


def consumer_task():
    consumer = ConsumerHandler()
    consumer.consume_and_upload()


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer_task)
    consumer_thread = threading.Thread(target=consumer_task)

    producer_thread.start()
    consumer_thread.start()

    # producer_thread.join()
    # consumer_thread.join()
