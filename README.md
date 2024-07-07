# RabbitMQ Producer-Consumer v1.0.0

This project demonstrates a simple RabbitMQ producer-consumer setup using Python and Docker.

## Version

v1.0.0

## Requirements

- Docker
- Docker Compose

## Setup and Run

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Build and start the Docker containers:

   ```bash
   docker-compose up -d
   ```

3. The producer will start sending messages to RabbitMQ every 5 seconds (configurable), and the consumer will log the received messages.

4. Access the RabbitMQ management interface at http://localhost:15672 (username: guest, password: guest).

## Configuration

- TYou can configure the message interval by setting the INTERVAL environment variable in the `docker-compose.yml` file.

## Configuration

- The producer logs each message before sending.
- The producer logs each message before sending.

## Clean Up

- To stop and remove the Docker containers, run:

  ```bash
  docker-compose down
  ```

## Notes

- Ensure Docker and Docker Compose are installed and running.
