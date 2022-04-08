from classic.app.errors import AppError


class NoBook(AppError):
	msg_template = "No books with id"
	code = 'Books.no_book'


class BookAlreadyBooked(AppError):
	msg_template = "Books is already booked"
	code = 'Books.already_booked'


class BooksNotBooked(AppError):
	msg_template = "Books not booked"
	code = 'Books.not_booked'

