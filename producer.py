import pika
import logging
import time
import json
import uuid
from datetime import datetime
import os

# Setup logging
logging.basicConfig(level=logging.INFO)

# RabbitMQ connection parameters
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
interval = int(os.getenv("INTERVAL", 5))  # Interval in seconds


def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=rabbitmq_host)
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            logging.error("Connection to RabbitMQ failed. Retrying in 5 seconds...")
            time.sleep(5)


def send_message():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    while True:
        message = {
            "message_id": str(uuid.uuid4()),
            "created_on": datetime.now().isoformat(),
        }
        channel.basic_publish(
            exchange="", routing_key="test_queue", body=json.dumps(message)
        )
        logging.info(f"Sent: {message}")
        time.sleep(interval)


if __name__ == "__main__":
    send_message()
