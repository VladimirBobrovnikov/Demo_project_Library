from classic.sql_storage import TransactionContext
from classic.messaging_kombu import KombuPublisher
from kombu import Connection

from adapters import RabbitMQ
from adapters import api
from application import services
from adapters.db.users.storage import UserRepo
from adapters.db import db__init
from adapters.api.settings import Settings


class DB:
	engine = db__init.engine
	db__init.metadata.create_all(engine)

	context = TransactionContext(bind=engine, expire_on_commit=False)

	user_repo = UserRepo(context=context)


class MessageBus:
	settings = RabbitMQ.Settings()
	connection = Connection(settings.BROKER_URL)
	RabbitMQ.broker_scheme.declare(connection)

	publisher = KombuPublisher(
		connection=connection,
		scheme=RabbitMQ.broker_scheme,
	)


class Application:
	users = services.UserService(
		users=DB.user_repo,
		publisher=MessageBus.publisher
	)


class Aspects:
	services.join_points.join(DB.context)
	api.join_points.join(MessageBus.publisher, DB.context)


app = api.create_app(
	is_dev_mode=False,
	users=Application.users)


if __name__ == "__main__":
	from wsgiref import simple_server

	with simple_server.make_server('127.0.0.1', 8080, app=app) as server:
		print('server with port 8080')
		server.serve_forever()
