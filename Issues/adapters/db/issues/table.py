from adapters.db.db__init import metadata

from sqlalchemy.orm import registry
from sqlalchemy import (
	Column,
	Integer,
	String,
	Table,
)

from application import dataclasses

actions = Table(
	'actions',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('body', String),
)

mapper_registry = registry()

mapper_registry.map_imperatively(dataclasses.Actions, actions)
