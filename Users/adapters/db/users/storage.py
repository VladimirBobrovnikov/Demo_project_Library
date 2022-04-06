from application import interfaces
from application.dataclasses import User
from application import errors
from classic.components import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, update
from attr import asdict

from typing import Optional, List


@component
class UserRepo(BaseRepository, interfaces.UsersRepo):
	def get_by_id(self, id_: int) -> Optional[User]:
		query = select(User).where(User.id == id_)
		return self.session.execute(query).scalars().one_or_none()

	def get_by_login(self, login: str, password: str) -> Optional[User]:
		query = select(User).where(User.login == login and User.password == password)
		return self.session.execute(query).scalars().one_or_none()

	def add(self, user: User):
		self.session.add(user)
		self.session.flush()
		self.session.refresh(user)
		return user

	def update(self, user: User):
		values = asdict(user)
		del values['id']
		query = update(User).where(User.id == user.id).values(**values)
		self.session.execute(query)

	def delete(self, id_: int):
		query = select(User).where(User.id == id_)
		user = self.session.execute(query).scalars().one_or_none()
		if user:
			self.session.delete(user)
		else:
			raise errors.NoUser

	def get_all(self) -> List[User]:
		query = select(User)
		return self.session.execute(query).scalars()
