from abc import ABC, abstractmethod
from typing import Optional, List

from .dataclasses import User


class UsersRepo(ABC):

	@abstractmethod
	def get_by_id(self, id_: int) -> Optional[User]:
		...

	@abstractmethod
	def get_by_login(self, login: str, password: str) -> Optional[User]:
		...

	@abstractmethod
	def add(self, user: User):
		...

	@abstractmethod
	def update(self, user: User):
		...

	@abstractmethod
	def delete(self, id_: int):
		...

	@abstractmethod
	def get_all(self) -> List[User]:
		...
