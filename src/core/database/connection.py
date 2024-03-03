from sqlmodel import create_engine

from src.constants import SQLITE_URL


engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})
