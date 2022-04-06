import attr
from typing import Optional
from datetime import datetime


@attr.dataclass
class IssueUser:
	user_id: int
	data_last_change: Optional[datetime] = None
	issue_id: Optional[int] = None
	books_reading: Optional['IssueBook'] = None
	deleted: bool = False


@attr.dataclass
class IssueBook:
	book_id: int
	data_last_change: Optional[datetime] = None
	issue_id: Optional[int] = None


@attr.dataclass
class Actions:
	body: str
	actions_id: Optional[int] = None
