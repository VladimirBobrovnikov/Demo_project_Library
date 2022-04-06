from abc import ABC, abstractmethod
from typing import Optional, List

from .dataclasses import IssueBook, IssueUser, Actions


class IssueBookRepo(ABC):

	@abstractmethod
	def get_by_id(self, id_: int) -> Optional[IssueBook]:
		...

	@abstractmethod
	def add(self, issue_book: IssueBook):
		...

	@abstractmethod
	def update(self, issue_book: IssueBook):
		...

	@abstractmethod
	def delete(self, id_: int):
		...

	@abstractmethod
	def get_all(self) -> List[IssueBook]:
		...

	@abstractmethod
	def get_all_reader(self, user_id) -> List[IssueUser]:
		...


class IssueUserRepo(ABC):

	@abstractmethod
	def get_by_id(self, id_: int) -> Optional[IssueUser]:
		...

	@abstractmethod
	def add(self, issue_user: IssueUser):
		...

	@abstractmethod
	def update_user_data(self):
		...

	@abstractmethod
	def update_user_rents(self, issue_user: IssueUser):
		...

	@abstractmethod
	def delete(self, user_id: int):
		...

	@abstractmethod
	def get_all(self) -> List[IssueUser]:
		...

	@abstractmethod
	def get_all_reading_book(self, user_id) -> List[IssueUser]:
		...


class LogsRepo(ABC):
	@abstractmethod
	def write_actions(self, actions: Actions):
		...

	@abstractmethod
	def get_action(self, actions_id: int) -> dict:
		...

	@abstractmethod
	def get_actions(self) -> List[Actions]:
		...
