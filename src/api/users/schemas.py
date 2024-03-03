from datetime import date, datetime
from pydantic import BaseModel


class CreateUserRequest(BaseModel):
	email: str
	password: str
	full_name: str
	date_of_birth: date


class CreateUserResponse(BaseModel):
	id: int
	email: str
	full_name: str
	date_of_birth: date
	created_at: datetime
	updated_at: datetime
