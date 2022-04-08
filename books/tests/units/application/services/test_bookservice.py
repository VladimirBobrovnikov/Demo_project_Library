import pytest
from attr import asdict
from application import errors
from application.services import BookService
from application import dataclasses
from unittest.mock import Mock


@pytest.fixture(scope='function')
def service1(books, publisher):
	return BookService(
		books=books,
		publisher=publisher)


book_DTO = {
	"title": "Война и мир",
	"author": "Л.Н.Толстой"
}

book_DTO_for_update = {
	"id": 1,
	"title": "Upd Война и мир"
}

data_book = {
	'id': 1,
	'title': "book_title",
	'author': "books_author",
	'tenants_id': None
}

book_1 = dataclasses.Book(
	id=1,
	title="book_title",
	author="books_author",
	tenants_id=None
)

book_2 = dataclasses.Book(
	id=2,
	title="book_title2",
	author="books_author2",
	tenants_id=1
)


def test__add_book(service1):
	service1.add_book(**book_DTO)
	service1.books.add.assert_called_once()


def test__get_book(service1):
	book_id = 1
	book = service1.get_book(book_id)
	assert asdict(book) == data_book


def test__update_book(service1):
	service1.update_book(**book_DTO_for_update)
	service1.books.update.assert_called_once()


def test__delete_book(service1):
	id_book = 1
	service1.delete_book(id_book)
	service1.books.delete.assert_called_once()


def test__get_books(service1):
	books = service1.books.get_all()
	assert books == [book_1, book_2]


def test__rent_book(service1):
	user_id = 1
	book_id = 1
	service1.rent_book(user_id, book_id)
	service1.books.update.assert_called_once()


def test__failed_rent_book(service1):
	user_id = 1
	book_id = 1
	service1.books.get_by_id = Mock(return_value=book_2)
	with pytest.raises(errors.BookAlreadyBooked):
		service1.rent_book(user_id, book_id)


def test__failed_2_rent_book(service1):
	user_id = 1
	book_id = 1
	service1.books.get_by_id = Mock(return_value=None)
	with pytest.raises(errors.NoBook):
		service1.rent_book(user_id, book_id)


def test__return_book(service1):
	user_id = 1
	book_id = 2
	service1.books.get_by_id = Mock(return_value=book_2)
	service1.return_book(user_id, book_id)
	service1.books.update.assert_called_once()


def test__failed_return_book(service1):
	user_id = 1
	book_id = 1
	with pytest.raises(errors.BooksNotBooked):
		service1.return_book(user_id, book_id)


def test__failed_2_return_book(service1):
	user_id = 1
	book_id = 1
	service1.books.get_by_id = Mock(return_value=None)
	with pytest.raises(errors.NoBook):
		service1.return_book(user_id, book_id)


