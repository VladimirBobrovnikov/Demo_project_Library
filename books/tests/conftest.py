import pytest
from application import dataclasses


@pytest.fixture(scope='function')
def book_with_id_1_without_tenants_id():
	return dataclasses.Book(
		id=1,
		title="book_title",
		author="books_author",
		tenants_id=None
	)

@pytest.fixture(scope='function')
def book_with_id_2_with_tenants_id():
	return dataclasses.Book(
		id=2,
		title="book_title2",
		author="books_author2",
		tenants_id=1
	)


