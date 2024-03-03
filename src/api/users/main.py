from fastapi import APIRouter
from sqlmodel import Session

from src.core.schemas.user import User
from src.core.database.connection import engine
from src.core.auth.passwords import hash_password

from .schemas import CreateUserRequest, CreateUserResponse

router = APIRouter(tags=["Users"])


@router.get("")
async def all():
	return [{"id": 1}]


@router.post("")
async def create(user_req: CreateUserRequest) -> CreateUserResponse:
	with Session(engine) as session:
		user = User(
			hashed_password=hash_password(user_req.password),
			**user_req.model_dump(exclude=["password"]),
		)

		session.add(user)
		session.commit()
		session.refresh(user)

		return user
