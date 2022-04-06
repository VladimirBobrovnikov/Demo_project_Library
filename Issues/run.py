from wsgiref import simple_server

from composites.issues_api import app

if __name__ == "__main__":
	with simple_server.make_server('0.0.0.0', 1236, app=app) as server:
		print('server with port 1236')
		server.serve_forever()


	#hupper -m waitress --port=8123 --host=127.0.0.1 messanger_api:app