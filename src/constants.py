from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
SCRIPTS_DIR = ROOT_DIR / "scripts"
TESTS_DIR = ROOT_DIR / "tests"
API_DIR = ROOT_DIR / "src" / "api"
CORE_DIR = ROOT_DIR / "src" / "api"

# Database settings
SQLITE_FILENAME = DATA_DIR / "database.db"
SQLITE_URL = f"sqlite:///{SQLITE_FILENAME}"

# Auth security
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
