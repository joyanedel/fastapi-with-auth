from sqlmodel import select, Session
from fastapi import APIRouter, Depends
from typing import Annotated

from src.core.schemas.brand import Brand
from src.core.schemas.user import User
from src.core.database.connection import engine
from src.core.auth.auth import get_current_user

router = APIRouter(tags=["Guitar Brand"])


@router.get("")
async def all(current_user: Annotated[User, Depends(get_current_user)]) -> list[Brand]:
	with Session(engine) as session:
		query = select(Brand)
		results = session.exec(query)

		return results.all()


@router.post("")
async def create(brand: Brand):
	with Session(engine) as session:
		session.add(brand)
		session.commit()
		session.refresh(brand)

		return brand
