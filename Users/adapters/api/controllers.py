from classic.components import component
from classic.http_auth import (
	authenticate,
	authenticator_needed
)

from application import services

from .join_points import join_point


@authenticator_needed
@component
class Users:
	users: services.UserService

	@join_point
	def on_post_create_user(self, request, response):
		token = self.users.add_user(**request.media)
		response.media = {
			'token': token
		}

	@join_point
	@authenticate
	def on_get_user(self, request, response, *args, **kwargs):
		user = self.users.get_user(request.context.client.user_id)
		response.media = {
			'id': user.id,
			'login': user.login,
			'name': user.name,
			'email': user.email,
			'date_registration': str(user.date_create)
		}

	@join_point
	@authenticate
	def on_post_update_user(self, request, response):
		self.users.update_user(id=request.context.client.user_id, **request.media)
		response.media = {
			'result': 'Successful updating'
		}

	@join_point
	@authenticate
	def on_post_delete_user(self, request, response):
		token = self.users.delete(id_=request.context.client.user_id)
		response.media = {
			'result': 'Successful deletion'
		}

	@join_point
	@authenticate
	def on_get_users(self, request, response, *args, **kwargs):
		users = self.users.get_all()
		response.media = {
			user.id: {
				'login': user.login,
				'email': user.email,
				'date_registration': str(user.date_create)
			} for user in users
		}

	@join_point
	def on_post_sign_in(self, request, response):
		token = self.users.sign_in(**request.media)
		response.media = {
			'token': token
		}
