from sqlmodel import SQLModel, Field
from typing import Optional


class Brand(SQLModel, table=True):
	id: Optional[str] = Field(primary_key=True, default=None)
	name: str
