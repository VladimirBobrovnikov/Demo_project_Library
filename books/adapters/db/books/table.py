from adapters.db.db__init import metadata

from sqlalchemy.orm import registry
from sqlalchemy import (
	Column,
	Integer,
	String,
	Table,
)

from application import dataclasses

book = Table(
	'books',
	metadata,
	Column('id', Integer, autoincrement=True, primary_key=True),
	Column('title', String),
	Column('author', String),
	Column('tenants_id', Integer, nullable=True),
)

mapper_registry = registry()

mapper_registry.map_imperatively(dataclasses.Book, book)
