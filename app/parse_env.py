import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER: Final[str] = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD: Final[str] = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST: Final[str] = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT: Final[int] = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB: Final[str] = os.getenv("POSTGRES_DB", "postgres")

POSTGRES_DSN: Final[str] = (
    f"postgres+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

