from fastapi import FastAPI

from src.api.users.main import router as users_router
from src.api.brands import router as brands_router
from src.api.auth.main import router as auth_router


app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")
app.include_router(brands_router, prefix="/brands")
