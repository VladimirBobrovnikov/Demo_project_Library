from classic.messaging_kombu import KombuConsumer
from kombu import Connection

from application import services

from .scheme import broker_scheme


def create_consumer(connection: Connection,
                    actions: services.ActionsService) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection,
                             scheme=broker_scheme)

    consumer.register_function(
        actions.get_message, 'BooksAction', 'UsersAction'
    )

    return consumer
