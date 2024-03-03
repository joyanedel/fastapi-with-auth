from sqlmodel import SQLModel

from src.core.schemas.brand import *  # noqa
from src.core.schemas.guitar import *  # noqa
from src.core.schemas.user import *  # noqa

from src.core.database.connection import engine


def create_db_and_tables():
	SQLModel.metadata.create_all(engine)
