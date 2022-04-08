from adapters.db.db__init import metadata

from sqlalchemy.orm import registry
from sqlalchemy.sql import func
from sqlalchemy import (
	Column,
	Integer,
	String,
	Table,
	TIMESTAMP
)

from application import dataclasses

user = Table(
	'users',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('login', String, unique=True),
	Column('password', String),
	Column('name', String),
	Column('email', String, nullable=True),
	Column('date_create', TIMESTAMP, server_default=func.now()),
)

mapper_registry = registry()

mapper_registry.map_imperatively(dataclasses.User, user)
