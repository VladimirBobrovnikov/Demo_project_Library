import attr
import json
from typing import Optional
from datetime import datetime


@attr.dataclass
class IssueUser:
	id: int
	data_last_change: Optional[datetime] = None
	books_read: Optional[str] = None
	deleted: bool = False


@attr.dataclass
class IssueBook:
	id: int
	data_last_change: Optional[datetime] = None
	tenants: Optional[str] = None


@attr.dataclass
class Actions:
	body: str
	actions_id: Optional[int] = None
