from fastapi import APIRouter

router = APIRouter(tags=["Users"])


@router.get("")
async def all():
	return [{"id": 1}]
