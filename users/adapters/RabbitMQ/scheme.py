from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue


broker_scheme = BrokerScheme(
    Queue('UsersAction', Exchange(name='users'), max_length=10),
)
