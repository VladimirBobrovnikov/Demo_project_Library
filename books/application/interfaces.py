from abc import ABC, abstractmethod
from typing import Optional, List

from .dataclasses import Book


class BooksRepo(ABC):

	@abstractmethod
	def get_by_id(self, id_: int) -> Optional[Book]:
		...

	@abstractmethod
	def add(self, book: Book):
		...

	@abstractmethod
	def update(self, book: Book):
		...

	@abstractmethod
	def delete(self, id_: int):
		...

	@abstractmethod
	def get_all(self) -> List[Book]:
		...
