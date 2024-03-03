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
