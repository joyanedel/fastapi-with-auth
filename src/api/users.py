from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def all():
	return [{"id": 1}]
