from sqlmodel import Session, select

from src.core.database.connection import engine
from src.core.schemas.user import User
from .passwords import verify_password
from .exceptions import UserNotFound


def authenticate_user(email: str, password: str) -> User:
	user = get_user_by_email(email)
	verify_password(password, user.hashed_password)

	return user


def get_user_by_email(email: str):
	with Session(engine) as session:
		query = select(User).where(User.email == email)
		result = session.exec(query).first()

		if result is None:
			raise UserNotFound(f"User with email {email} not found")

		return result
