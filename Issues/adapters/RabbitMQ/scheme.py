from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue


broker_scheme = BrokerScheme(
    Queue('BooksAction', Exchange(name='books'), max_length=10),
    Queue('UsersAction', Exchange(name='users'), max_length=10),
)
