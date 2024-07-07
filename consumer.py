import pika
import logging
import os
import time
import json

# Setup logging
logging.basicConfig(level=logging.INFO)

# RabbitMQ connection parameters
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")


def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.info(f"Received: {message}")


def start_consuming():
    connection = None
    while connection is None:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=rabbitmq_host)
            )
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Connection to RabbitMQ failed: {e}")
            time.sleep(5)
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    channel.basic_consume(
        queue="test_queue", on_message_callback=callback, auto_ack=True
    )
    logging.info("Waiting for messages...")
    channel.start_consuming()


if __name__ == "__main__":
    start_consuming()
