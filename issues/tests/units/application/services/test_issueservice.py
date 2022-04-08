import pytest
from application.services import ActionsService


@pytest.fixture(scope='function')
def service1(issue_book_repo, issue_user_repo, actions):
	return ActionsService(
		issue_book_repo=issue_book_repo,
		issue_user_repo=issue_user_repo,
		actions=actions
	)


data_add_user = {
	'routing_key': 'users.add',
	'add': {
		'login': 'vova',
		'password': '1234',
		'name': 'vova',
		'email': None,
		'id': 1,
		'date_create': '2022-04-07T12:24:33.350502'
	}
}
data_update_user = {
	'routing_key': 'users.update',
	'update': {
		'login': 'vova',
		'password': '1234',
		'name': 'vova',
		'email': 'vova@mail.ru',
		'id': 1,
		'date_create': '2022-04-07T12:24:33.350502'
	}
}

data_add_book = {
	'routing_key': 'books.add',
	'add': {
		'title': 'Война и мир',
		'author': 'Л.Н.Толстой',
		'tenants_id': None,
		'id': 1
	}
}

data_rent_book = {
	'routing_key': 'books.rent',
	'rent': {'id': 1, 'tenants_id': 1}
}

def test__get_message(service1):
	service1.get_message(data_add_user)
	service1.actions.write_actions.assert_called_once()
	service1.issue_user_repo.add.assert_called_once()


def test__get_message_2(service1):
	service1.get_message(data_update_user)
	service1.actions.write_actions.assert_called_once()
	service1.issue_user_repo.update_user_data.assert_called_once()


def test__get_message_3(service1):
	service1.get_message(data_add_book)
	service1.actions.write_actions.assert_called_once()
	service1.issue_book_repo.add.assert_called_once()


def test__get_message_4(service1):
	service1.get_message(data_rent_book)
	service1.actions.write_actions.assert_called_once()
	service1.issue_book_repo.rent.assert_called_once()
	service1.issue_user_repo.update_user_rents.assert_called_once()

