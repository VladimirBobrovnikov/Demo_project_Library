from classic.app.errors import AppError


class NoBook(AppError):
	msg_template = "No books with id '{id}'"
	code = 'Books.no_book'


