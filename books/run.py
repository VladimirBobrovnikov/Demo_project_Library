from wsgiref import simple_server

from composites.books_api import app

if __name__ == "__main__":
	with simple_server.make_server('0.0.0.0', 1235, app=app) as server:
		print('server with port 1235')
		server.serve_forever()

