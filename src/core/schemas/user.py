from datetime import date
from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
	id: Optional[int] = Field(primary_key=True, default=None)
	email: str
	hashed_password: str

	full_name: str
	date_of_birth: date
