import falcon
from classic.components import component
from classic.http_auth import (
	authenticate,
	authenticator_needed,
)

from application import services

from .join_points import join_point


@authenticator_needed
@component
class Books:
	books: services.BookService

	@authenticate
	@join_point
	def on_post_add_book(self, request, response):
		book = self.books.add_book(**request.media)
		response.media = {
			'result': 'Successful addition'
		}

	@authenticate
	@join_point
	def on_post_rent_book(self, request, response):
		book = self.books.rent_book(user_id=request.context.client.user_id, **request.media)
		response.media = {
			'result': 'Successful booking'
		}

	@authenticate
	@join_point
	def on_post_update_book(self, request, response):
		self.books.update_book(**request.media)
		response.media = {
			'result': 'Successful updating'
		}

	@authenticate
	@join_point
	def on_post_delete_book(self, request, response):
		self.books.delete_book(**request.media)
		response.media = {
			'result': 'Successful deletion'
		}

	@join_point
	@authenticate
	def on_get_book(self, request, response, *args, **kwargs):
		book = self.books.get_book(**request.params)
		if book:
			response.media = {
				'id': book.id,
				'title': book.title,
				'author': book.author,
				'tenants_id': book.tenants_id,
			}
		else:
			response.media = {
				'Exception': 'Book not found'
			}
			response.status = falcon.HTTPNotFound

	@join_point
	@authenticate
	def on_get_books(self, request, response, *args, **kwargs):
		books = self.books.get_books(**request.params)
		response.media = {
			book.id: {
				'title': book.title,
				'author': book.author,
				'tenants_id': book.tenants_id,
			} for book in books
		}

	@authenticate
	@join_point
	def on_post_return_book(self, request, response):
		self.books.return_book(user_id=request.context.client.user_id, **request.media)
		response.media = {
			'result': 'Books returned success'
		}
