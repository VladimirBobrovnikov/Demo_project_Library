from application import interfaces
from application.dataclasses import Book
from application import errors
from classic.components import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, update
from attr import asdict

from typing import Optional, List


@component
class BookRepo(BaseRepository, interfaces.BooksRepo):
	def get_by_id(self, id_: int) -> Optional[Book]:
		query = select(Book).where(Book.id == id_)
		return self.session.execute(query).scalars().one_or_none()

	def add(self, book: Book):
		self.session.add(book)
		self.session.flush()
		self.session.refresh(book)
		return book

	def update(self, book: Book):
		values = asdict(book)
		del values['id']
		query = update(Book).where(Book.id == book.id).values(**values)
		self.session.execute(query)

	def delete(self, id_: int):
		query = select(Book).where(Book.id == id_)
		book = self.session.execute(query).scalars().one_or_none()
		if book:
			self.session.delete(book)
		else:
			raise errors.NoBook

	def get_all(self) -> List[Book]:
		query = select(Book)
		return self.session.execute(query).scalars()
