from classic.components import component
from classic.aspects import PointCut
from classic.app import DTO, validate_with_dto

from typing import Optional

from . import interfaces
from . import errors
from .dataclasses import Actions, IssueUser, IssueBook

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
	id: int
	login: str
	password: str
	name: str
	email: Optional[str] = None
	date_create: Optional[str] = None


class BookInfo(DTO):
	id: int
	title: str
	author: str
	tenants_id: Optional[int] = None


class BookInfoForDelete(DTO):
	id: int


class UserInfoForDelete(DTO):
	id: int


class ChangeRentStatusInfo(DTO):
	id: int
	tenants_id: Optional[int]


@component
class ActionsService:
	actions: interfaces.LogsRepo
	issue_user_repo: interfaces.IssueUserRepo
	issue_book_repo: interfaces.IssueBookRepo

	def _pars_users_action(self, actions: str):
		action_dict = {
			'add': self._add_users_issue,
			'update': self._update_users_issue,
			'delete': self._delete_user_issue,
		}
		return action_dict[actions]

	def _pars_books_action(self, actions):
		action_dict = {
			'add': self._add_books_issue,
			'update': self._update_book_issue,
			'delete': self._delete_book_issue,
			'rent': self._rent_book_issue,
			'return': self._return_book_issue
		}
		return action_dict[actions]

	@join_point
	@validate_with_dto
	def _add_users_issue(self, user_info: UserInfo):
		user = IssueUser(user_info.id)
		self.issue_user_repo.add(user)

	@join_point
	@validate_with_dto
	def _update_users_issue(self, user_info: UserInfo):
		self.issue_user_repo.update_user_data(user_info.id)

	@join_point
	@validate_with_dto
	def _delete_user_issue(self, user_info: UserInfoForDelete):
		self.issue_user_repo.delete(user_info.id)

	@join_point
	@validate_with_dto
	def _add_books_issue(self, book_info: BookInfo):
		book = IssueBook(book_info.id)
		self.issue_book_repo.add(book)

	@join_point
	@validate_with_dto
	def _update_book_issue(self, book_info: BookInfo):
		self.issue_book_repo.update(book_info.id)

	@join_point
	@validate_with_dto
	def _delete_book_issue(self, book_info: BookInfoForDelete):
		self.issue_book_repo.delete(book_info.id)

	@join_point
	@validate_with_dto
	def _rent_book_issue(self, rent_status: ChangeRentStatusInfo):
		self.issue_book_repo.rent(rent_status.id, rent_status.tenants_id)
		self.issue_user_repo.update_user_rents(rent_status.tenants_id, rent_status.id)

	@join_point
	@validate_with_dto
	def _return_book_issue(self, rent_status: ChangeRentStatusInfo):
		self.issue_book_repo.update(rent_status.id)

	@join_point
	def get_message(self, data):
		queue_dict = {
			'books': self._pars_books_action,
			'users': self._pars_users_action
		}

		routing_key: str = data['routing_key']
		queue_name, actions = routing_key.split('.')

		self.actions.write_actions(Actions(str({actions: data[actions]})))

		parser = queue_dict[queue_name]
		func = parser(actions)
		func(**data[actions])
