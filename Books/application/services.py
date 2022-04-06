from classic.components import component
from classic.aspects import PointCut
from classic.messaging import Publisher, Message
from classic.app import DTO, validate_with_dto
from pydantic import validate_arguments
from attr import asdict

from typing import Optional

from . import interfaces
from . import errors
from .dataclasses import Book

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
	title: str
	author: str
	tenants_id: Optional[int] = None
	id: Optional[int] = None


class BookInfoForUpdate(DTO):
	id: int
	title: Optional[str] = None
	author: Optional[str] = None
	tenants_id: Optional[int] = None


@component
class BookService:
	books: interfaces.BooksRepo
	publisher: Publisher

	@join_point
	@validate_with_dto
	def add_book(self, book_info: BookInfo):
		book = book_info.create_obj(Book)
		book = self.books.add(book)
		body = {
			'data': {
				'routing_key': 'books.add',
				'add': asdict(book)
			}
		}
		self.publisher.plan(
			Message('books', body)
		)
		return book

	@join_point
	@validate_arguments
	def get_book(self, book_id: int) -> Optional[Book]:
		return self.books.get_by_id(book_id)

	@join_point
	@validate_with_dto
	def update_book(self, book_info: BookInfoForUpdate):
		old_book = self.books.get_by_id(book_info.id)
		if old_book:
			if book_info.title:
				old_book.title = book_info.title
			if book_info.author:
				old_book.author = book_info.author
			if book_info.tenants_id:
				old_book.tenants_id = book_info.tenants_id
			self.books.update(old_book)
			body = {
				'data': {
					'routing_key': 'books.update',
					'update': asdict(old_book)
				}
			}
			self.publisher.plan(
				Message('books', body)
			)
		else:
			raise errors.NoBook

	@join_point
	@validate_arguments
	def delete_book(self, id_: int):
		self.books.delete(id_)
		body = {
			'data': {
				'routing_key': 'books.delete',
				'delete': id_
			}
		}
		self.publisher.plan(
			Message('books', body)
		)

	@join_point
	def get_books(self):
		return self.books.get_all()

	@join_point
	def rent_book(self, user_id: int, book_id: int):
		book = self.books.get_by_id(book_id)
		if book and book.tenants_id is None:
			book.tenants_id = user_id
			self.books.update(book)
			body = {
				'data': {
					'routing_key': 'books.rent',
					'rent': {
						'book_id': book.id,
						'tenants_id': book.tenants_id
					}
				}
			}
			self.publisher.plan(
				Message('books', body)
			)

	@join_point
	def return_book(self, user_id: int, book_id: int):
		book = self.books.get_by_id(book_id)
		if book and book.tenants_id == user_id:
			book.tenants_id = None
			self.books.update(book)
			body = {
				'data': {
					'routing_key': 'books.return',
					'return': {
						'book_id': book.id,
						'tenants_id': 'None'
					}
				}
			}
			self.publisher.plan(
				Message('books', body)
			)


