from datetime import timedelta, datetime
from typing import Optional
from jose import jwt
from src.core.auth.schemas import Token
from src.constants import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


def create_token(data: dict):
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(data, access_token_expires)

	return Token(access_token=access_token, token_type="bearer")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
	target_to_encode_data = data.copy()
	expires = datetime.utcnow() + expires_delta
	target_to_encode_data.update({"exp": expires})
	encoded_jwt = jwt.encode(target_to_encode_data, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt
