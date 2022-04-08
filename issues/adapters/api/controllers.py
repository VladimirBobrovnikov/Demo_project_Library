import falcon
from classic.components import component
from classic.http_auth import (
	authenticate,
	authenticator_needed,
)

from application import services

from .join_points import join_point


@component
class Actions:
	actions: services.ActionsService

