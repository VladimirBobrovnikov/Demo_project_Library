from adapters.db.db__init import metadata

from sqlalchemy.orm import registry
from sqlalchemy import (
	Column,
	Integer,
	String,
	Table,
	TIMESTAMP,
)
from sqlalchemy.dialects.postgresql import JSON
from application import dataclasses
from sqlalchemy.sql import func


actions = Table(
	'actions',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('body', String),
)


issue_user = Table(
	'issue_user',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('modified_date', TIMESTAMP, server_default=func.now(), onupdate=func.now()),
	Column('books_read', JSON, nullable=True)
)

issue_book = Table(
	'issue_book',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('modified_date', TIMESTAMP, server_default=func.now(), onupdate=func.now()),
	Column('tenants', JSON, nullable=True)
)


mapper_registry = registry()

mapper_registry.map_imperatively(dataclasses.Actions, actions)
mapper_registry.map_imperatively(dataclasses.IssueUser, issue_user)
mapper_registry.map_imperatively(dataclasses.IssueBook, issue_book)
