from sqlmodel import select, Session
from fastapi import APIRouter

from src.core.schemas.brand import Brand
from src.core.database.connection import engine

router = APIRouter(tags=["Guitar Brand"])


@router.get("")
async def all() -> list[Brand]:
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
