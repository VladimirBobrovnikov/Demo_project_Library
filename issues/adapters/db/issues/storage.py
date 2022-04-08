from datetime import datetime

from application import interfaces
from application.dataclasses import Actions, IssueUser, IssueBook
from application import errors
from classic.components import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, update, delete
from attr import asdict

from typing import List, Optional
import json

@component
class LogsRepo(BaseRepository, interfaces.LogsRepo):
	def write_actions(self, actions: Actions):
		self.session.add(actions)
		self.session.flush()
		self.session.refresh(actions)
		return actions

	def get_action(self, actions_id: int) -> dict:
		query = select(Actions).where(Actions.actions_id == actions_id)
		return self.session.execute(query).scalars().one_or_none()

	def get_actions(self) -> List[dict]:
		query = select(Actions)
		return self.session.execute(query).scalars()


@component
class IssueUserRepo(BaseRepository, interfaces.IssueUserRepo):
	def get_by_id(self, id_: int) -> Optional[IssueUser]:
		query = select(IssueUser).where(IssueUser.id == id_)
		return self.session.execute(query).scalars().one_or_none()

	def add(self, issue_user: IssueUser):
		self.session.add(issue_user)
		self.session.flush()
		self.session.refresh(issue_user)
		return issue_user

	def update_user_data(self, id: int):
		query = update(IssueUser).where(IssueUser.id == id).values()
		self.session.execute(query)

	def update_user_rents(self, id_user: int, id_book: int):
		query = select(IssueUser).where(IssueUser.id == id_user)
		obj = self.session.execute(query).scalars().one_or_none()
		data = dict()
		data_in_json = obj.books_read
		if data_in_json:
			data = json.loads(data_in_json)
		data[id_book] = None
		query = update(IssueUser).where(IssueUser.id == id_user).values(books_read=json.dumps(data))
		self.session.execute(query)

	def delete(self, user_id: int):
		query = delete(IssueUser).where(IssueUser.id == user_id)
		self.session.execute(query)

	def get_all(self) -> List[IssueUser]:
		query = select(IssueUser)
		return self.session.execute(query).scalars()

	def get_all_reading_book(self, user_id) -> dict:
		query = select(IssueUser).where(IssueUser.id == user_id)
		obj = self.session.execute(query).scalars().one_or_none()
		data_in_json = obj.books_read
		if data_in_json:
			return json.loads(data_in_json)


@component
class IssueBookRepo(BaseRepository, interfaces.IssueBookRepo):
	def get_by_id(self, id_: int) -> Optional[IssueBook]:
		query = select(IssueBook).where(IssueBook.id == id_)
		return self.session.execute(query).scalars().one_or_none()

	def add(self, issue_book: IssueBook):
		self.session.add(issue_book)
		self.session.flush()
		self.session.refresh(issue_book)
		return issue_book

	def update(self, id: int):
		query = update(IssueBook).where(IssueBook.id == id).values()
		self.session.execute(query)

	def rent(self, id_book: int, id_user: int):
		query = select(IssueBook).where(IssueBook.id == id_book)
		obj = self.session.execute(query).scalars().one_or_none()
		readers = dict()
		data_in_json = obj.tenants
		if data_in_json:
			readers = json.loads(data_in_json)
		readers[id_user] = None
		query = update(IssueBook).where(IssueBook.id == id_book).values(tenants=json.dumps(readers))
		self.session.execute(query)

	def delete(self, id_: int):
		query = delete(IssueBook).where(IssueBook.id == id_)
		self.session.execute(query)

	def get_all(self) -> List[IssueBook]:
		query = select(IssueBook)
		return self.session.execute(query).scalars()

	def get_all_reader(self, id_book) -> List[int]:
		query = select(IssueBook).where(IssueBook.id == id_book)
		obj = self.session.execute(query).scalars().one_or_none()
		data_in_json = obj.tenants
		return list((json.loads(data_in_json)).keys())

