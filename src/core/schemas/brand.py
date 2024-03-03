from sqlmodel import SQLModel, Field
from typing import Optional


class Brand(SQLModel, table=True):
	id: Optional[int] = Field(primary_key=True, default=None)
	name: str
