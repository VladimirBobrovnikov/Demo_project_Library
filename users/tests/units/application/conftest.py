from unittest.mock import Mock
from classic.messaging import Publisher

import pytest

from application import interfaces


@pytest.fixture(scope='function')
def users(user_with_id_1, user_with_id_2):
	users = Mock(interfaces.UsersRepo)
	users.get_by_id = Mock(return_value=user_with_id_1)
	users.get_by_login = Mock(return_value=user_with_id_1)
	users.get_all = Mock(return_value=[user_with_id_1, user_with_id_2])
	users.add = Mock(return_value=user_with_id_1)
	return users


@pytest.fixture(scope='function')
def publisher():
	publisher = Mock(Publisher)
	publisher.plan = Mock(return_value=None)
	return publisher
