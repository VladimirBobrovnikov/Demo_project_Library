import attr
import datetime
from typing import Optional


@attr.dataclass
class User:
	login: str
	password: str
	name: str
	email: Optional[str] = None
	id: Optional[int] = None
	date_create: Optional[datetime.datetime] = None
