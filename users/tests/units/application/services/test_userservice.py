import pytest
from attr import asdict
from application.services import UserService
from application import dataclasses
from datetime import datetime


@pytest.fixture(scope='function')
def service1(users, publisher):
	return UserService(
		users=users,
		publisher=publisher)


user_DTO = {
	"login": "vova",
	"password": 1234,
	"name": "vova"
}

user_DTO_for_sign_in = {
	"login": "vova",
	"password": 1234,
}


user_DTO_for_update = {
	"email": "vova@mail.ru"
}

data_user = {
	"id": 1,
	"login": "vova",
	"password": '1234',
	"name": "vova",
	'email': None,
	'date_create': datetime(2022, 4, 7, 16, 39, 14, 989636)
}

user_1 = dataclasses.User(login='vova', password='1234', name='vova', email=None, id=1, date_create=datetime(2022, 4, 7, 16, 39, 14, 989636))
user_2 = dataclasses.User(login='gora', password='1234', name='Igor', email='igor@mail.ru', id=2, date_create=datetime(2022, 4, 7, 16, 48, 0, 327654))


def test__sign_in(service1):
	token = service1.sign_in(**user_DTO_for_sign_in)
	assert token == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImxvZ2luIjoidm92YSIsIm5hbWUiOiJ2b3ZhIiwicGFzc3dvcmQiOiIxMjM0IiwiZ3JvdXBzIjoiYWRtaW5zIn0.9CoutgnPd2n89dwd-4Hw3armwf3yYIlGRHQ9bMeUvb0"


def test__add_user(service1):
	token = service1.add_user(**user_DTO)
	assert token == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImxvZ2luIjoidm92YSIsIm5hbWUiOiJ2b3ZhIiwicGFzc3dvcmQiOiIxMjM0IiwiZ3JvdXBzIjoiYWRtaW5zIn0.9CoutgnPd2n89dwd-4Hw3armwf3yYIlGRHQ9bMeUvb0"


def test__get_user(service1):
	user_id = 1
	user = service1.get_user(user_id)
	assert asdict(user) == data_user


def test__update_user(service1):
	service1.update_user(id=1, **user_DTO_for_update)
	service1.users.update.assert_called_once()


def test__delete(service1):
	id_user = 1
	service1.delete(id_user)
	service1.users.delete.assert_called_once()


def test__get_all(service1):
	users = service1.get_all()
	assert users == [user_1, user_2]
