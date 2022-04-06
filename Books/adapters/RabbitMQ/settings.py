from pydantic import BaseSettings
import os


username = os.getenv('RABBITMQ_USERNAME', 'user')
password = os.getenv('RABBITMQ_PASSWORD', 'password')
host = os.getenv('RABBITMQ_HOST', '127.0.0.1')
port = os.getenv('RABBITMQ_PORT', '5672')


RabbitMQ_URL = f'amqp://{username}:{password}@{host}:{port}'


class Settings(BaseSettings):
    BROKER_URL: str = RabbitMQ_URL
