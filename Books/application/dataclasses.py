import attr
from typing import Optional


@attr.dataclass
class Book:
	title: str
	author: str
	tenants_id: Optional[int] = None
	id: Optional[int] = None
