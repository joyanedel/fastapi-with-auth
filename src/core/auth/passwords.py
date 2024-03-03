import logging

from passlib.context import CryptContext

from .exceptions import IncorrectPassword

logging.getLogger("passlib").setLevel(logging.ERROR)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_password: str):
	"""Check if password is valid, if not then raise an exception"""
	is_correct_password = pwd_context.verify(password, hashed_password)
	if not is_correct_password:
		raise IncorrectPassword()


def hash_password(password: str) -> str:
	return pwd_context.hash(password)
