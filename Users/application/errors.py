from classic.app.errors import AppError


class NoUser(AppError):
	msg_template = "No users with id '{id}'"
	code = 'Users.no_user'


