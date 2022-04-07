import pytest
from Users.application import dataclasses
from datetime import datetime

@pytest.fixture(scope='function')
def user_with_id_1():
	return dataclasses.User(
		id=1,
		login="vova",
		password="1234",
		name="vova",
		email=None,
		date_create=datetime(2022, 4, 7, 16, 39, 14, 989636)
	)


@pytest.fixture(scope='function')
def user_with_id_2():
	return dataclasses.User(
		id=2,
		login="gora",
		password="1234",
		name="Igor",
		email='igor@mail.ru',
		date_create=datetime(2022, 4, 7, 16, 48, 0, 327654)
	)
