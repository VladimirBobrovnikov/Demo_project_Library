from unittest.mock import Mock
from classic.messaging import Publisher

import pytest

from Books.application import interfaces


@pytest.fixture(scope='function')
def books(book_with_id_1_without_tenants_id, book_with_id_2_with_tenants_id):
	books = Mock(interfaces.BooksRepo)
	books.get_by_id = Mock(return_value=book_with_id_1_without_tenants_id)
	books.get_all = Mock(return_value=[book_with_id_1_without_tenants_id, book_with_id_2_with_tenants_id])
	return books


@pytest.fixture(scope='function')
def publisher():
	publisher = Mock(Publisher)
	publisher.plan = Mock(return_value=None)
	return publisher
