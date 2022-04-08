import pytest
from application import dataclasses
from datetime import datetime


@pytest.fixture(scope='function')
def issue_book_with_id_1():
	return dataclasses.IssueBook(
		id=1,
		data_last_change=datetime(2022, 4, 7, 16, 39, 14, 989636)
	)


@pytest.fixture(scope='function')
def issue_user_with_id_1():
	return dataclasses.IssueUser(
		id=1,
		data_last_change=datetime(2022, 4, 7, 16, 39, 14, 989636)
	)


@pytest.fixture(scope='function')
def action_with_id_1():
	return dataclasses.Actions(
		actions_id=1,
		body="'add': {'login': 'vova', 'password': '1234', 'name': 'vova', 'email': None, 'id': 1, 'date_create': '2022-04-07T12:24:33.350502'}"
	)
