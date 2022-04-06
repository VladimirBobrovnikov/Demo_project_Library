from application import interfaces
from application.dataclasses import Actions
from application import errors
from classic.components import component
from classic.sql_storage.repository import BaseRepository
from sqlalchemy import select, update
from attr import asdict

from typing import List


@component
class LogsRepo(BaseRepository, interfaces.LogsRepo):
	def write_actions(self, actions: Actions):
		self.session.add(actions)
		self.session.flush()
		self.session.refresh(actions)
		return actions

	def get_action(self, actions_id: int) -> dict:
		query = select(Actions).where(Actions.actions_id == actions_id)
		return self.session.execute(query).scalars().one_or_none()

	def get_actions(self) -> List[dict]:
		query = select(Actions)
		return self.session.execute(query).scalars()

