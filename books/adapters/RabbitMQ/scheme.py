from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue


broker_scheme = BrokerScheme(
    Queue('BooksAction', Exchange(name='books'), max_length=10),
)
