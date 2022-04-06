from classic.sql_storage import TransactionContext
from classic.messaging_kombu import KombuPublisher
from kombu import Connection

from adapters import api
from adapters import RabbitMQ
from application import services
from adapters.db.issues.storage import LogsRepo
from adapters.db import db__init

import threading


class DB:
	engine = db__init.engine
	db__init.metadata.create_all(engine)

	context = TransactionContext(bind=engine, expire_on_commit=False)

	actions = LogsRepo(context=context)


class Application:
	actions = services.ActionsService(
		actions=DB.actions,
	)


class MessageBus:
	settings = RabbitMQ.Settings()
	connection = Connection(settings.BROKER_URL)
	RabbitMQ.broker_scheme.declare(connection)

	consumer = RabbitMQ.create_consumer(
		connection, Application.actions
	)


class Aspects:
	services.join_points.join(DB.context)
	api.join_points.join(DB.context)


thread = threading.Thread(target=MessageBus.consumer.run, daemon=True)

app = api.create_app(
	is_dev_mode=False,
	actions=Application.actions
)

thread.start()

if __name__ == "__main__":
	from wsgiref import simple_server

	with simple_server.make_server('127.0.0.1', 8081, app=app) as server:
		print('server with port 8081')
		server.serve_forever()
