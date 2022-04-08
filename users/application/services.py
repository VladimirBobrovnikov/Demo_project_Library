import os
from typing import Optional, List
import datetime

from classic.components import component
from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.messaging import Publisher, Message
from pydantic import validate_arguments
import jwt
from attr import asdict

from . import interfaces
from . import errors
from .dataclasses import User


join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
	id: int
	login: Optional[str] = None
	password: Optional[str] = None
	name: Optional[str] = None
	email: Optional[str] = None


class UserInfoForCreate(DTO):
	login: str
	password: str
	name: str
	email: Optional[str] = None
	date_create: Optional[datetime.date] = None


class UserInfoForSignIn(DTO):
	login: str
	password: str


@component
class UserService:
	users: interfaces.UsersRepo
	publisher: Publisher

	@staticmethod
	def _create_token(id_: int, login: str, name: str, password: str, groups: str):
		payload = {
			"sub": id_,
			'login': login,
			'name': name,
			'password': password,
			'groups': groups,
		}
		token = jwt.encode(payload=payload, key=str(os.getenv('SECRET_KEY')))
		return token

	@join_point
	@validate_with_dto
	def sign_in(self, user_info: UserInfoForSignIn) -> str:
		user = self.users.get_by_login(user_info.login, user_info.password)
		token = self._create_token(user.id, user.login, user.name, user.password, 'admins')
		return token

	@join_point
	@validate_with_dto
	def add_user(self, user_info: UserInfoForCreate):
		user = user_info.create_obj(User)
		user = self.users.add(user)
		token = self._create_token(user.id, user.login, user.name, user.password, 'admins')
		body = {'data': {
			'routing_key': 'users.add',
			'add': asdict(user)
			}
		}
		self.publisher.plan(
			Message('users', body)
		)
		return token

	@join_point
	@validate_arguments
	def get_user(self, id_: int) -> Optional[User]:
		return self.users.get_by_id(id_)

	@join_point
	@validate_with_dto
	def update_user(self, user_info: UserInfo):
		old_user = self.users.get_by_id(user_info.id)
		if old_user:
			if user_info.login:
				old_user.login = user_info.login
			if user_info.password:
				old_user.password = user_info.password
			if user_info.name:
				old_user.name = user_info.name
			if user_info.email:
				old_user.email = user_info.email
			self.users.update(old_user)
			body = {
				'data': {
					'routing_key': 'users.update',
					'update': asdict(old_user)
				}
			}
			self.publisher.plan(
				Message('users', body)
			)

		else:
			raise errors.NoUser

	@join_point
	@validate_arguments
	def delete(self, id_: int):
		self.users.delete(id_)
		body = {
			'data': {
				'routing_key': 'users.delete',
				'delete': {'id': id_}
			}
		}
		self.publisher.plan(
			Message('users', body)
		)

	@join_point
	def get_all(self) -> List[User]:
		return self.users.get_all()
