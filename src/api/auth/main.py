from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from src.core.auth.schemas import Token
from src.core.auth.login import authenticate_user
from src.core.auth.exceptions import AuthenticationFailed


router = APIRouter(tags=["Authentication"])

a = True


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
	try:
		user = authenticate_user(form_data.username, form_data.password)
	except AuthenticationFailed as exc:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Incorrect username or password",
			headers={"WWW-Authenticate": "Bearer"},
		) from exc

	return Token(access_token="a", token_type="bearer")


@router.post("/refresh-token")
async def refresh_token(): ...
