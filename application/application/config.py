import os

from dotenv import load_dotenv
from pydantic import AnyHttpUrl

load_dotenv()

POSTGRES_NAME: str = os.getenv("POSTGRES_NAME", default="postgres")
_DATABASE_USER: str = os.getenv("POSTGRES_USER", default="postgres")
_DATABASE_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", default="postgres")
POSTGRES_DB: str = os.getenv("POSTGRES_DB", default="localhost")
POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", default="5432")

BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = os.getenv(
    "POSTGRES_USER", default="http://127.0.0.1:8888 http://localhost"
).split()

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+asyncpg://{_DATABASE_USER}:"
    f"{_DATABASE_PASSWORD}@"
    f"{POSTGRES_DB}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_NAME}"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PAGINATION_SIZE = 10
