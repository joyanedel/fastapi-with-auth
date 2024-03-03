from sqlmodel import select, Session
from fastapi import APIRouter
from core.schemas.brand import Brand


router = APIRouter()


@router.get("")
async def all():
	with Session(...) as session:
		query = select(Brand)
		results = session.exec(query)

		return results.all()
