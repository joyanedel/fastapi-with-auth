from sqlmodel import SQLModel, Field
from typing import Optional


class Guitar(SQLModel, table=True):
	id: Optional[int] = Field(primary_key=True, default=None)
	model: str
	year: int
	frets: int
	pickups: int
	strings: int
	color: str
