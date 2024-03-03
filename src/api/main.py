from fastapi import FastAPI

from src.api.users import router as users_router
from src.api.brands import router as brands_router


app = FastAPI()

app.include_router(users_router, prefix="/users")
app.include_router(brands_router, prefix="/brands")
