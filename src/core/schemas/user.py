from datetime import date, datetime
from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
	id: Optional[int] = Field(primary_key=True, default=None)
	email: str
	hashed_password: str

	full_name: str
	date_of_birth: date

	created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
	updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
