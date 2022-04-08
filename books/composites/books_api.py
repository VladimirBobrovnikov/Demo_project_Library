from classic.sql_storage import TransactionContext
from classic.messaging_kombu import KombuPublisher
from kombu import Connection

from adapters import api
from adapters import RabbitMQ
from application import services
from adapters.db.books.storage import BookRepo
from adapters.db import db__init


class DB:
	engine = db__init.engine
	db__init.metadata.create_all(engine)

	context = TransactionContext(bind=engine, expire_on_commit=False)

	book_repo = BookRepo(context=context)


class MessageBus:
	settings = RabbitMQ.Settings()
	connection = Connection(settings.BROKER_URL)
	RabbitMQ.broker_scheme.declare(connection)

	publisher = KombuPublisher(
		connection=connection,
		scheme=RabbitMQ.broker_scheme,
	)


class Application:
	books = services.BookService(
		books=DB.book_repo,
		publisher=MessageBus.publisher
	)


class Aspects:
	services.join_points.join(DB.context)
	api.join_points.join(MessageBus.publisher, DB.context)


app = api.create_app(
	is_dev_mode=False,
	books=Application.books
)

if __name__ == "__main__":
	from wsgiref import simple_server

	with simple_server.make_server('127.0.0.1', 8082, app=app) as server:
		print('server with port 8082')
		server.serve_forever()
