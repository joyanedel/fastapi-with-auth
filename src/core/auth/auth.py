from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlmodel import Session, select
from jose import jwt, JWTError

from src.core.database.connection import engine
from src.core.schemas.user import User
from src.constants import SECRET_KEY, ALGORITHM
from .passwords import verify_password
from .exceptions import UserNotFound


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")


def authenticate_user(email: str, password: str) -> User:
	user = get_user_by_email(email)
	verify_password(password, user.hashed_password)

	return user


def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email: str = payload.get("sub")
		user = get_user_by_email(email)
	except JWTError as exc:
		raise Exception() from exc
	except UserNotFound as exc:
		raise Exception() from exc

	return user


def get_user_by_email(email: str):
	with Session(engine) as session:
		query = select(User).where(User.email == email)
		result = session.exec(query).first()

		if result is None:
			raise UserNotFound(f"User with email {email} not found")

		return result
