import os
from dotenv import dotenv_values

# Load from .env file (as fallback)
fallback_env = dotenv_values(".env")


def get_env_var(key, fallback_dict=fallback_env):
    """Retrieves the value of an environment variable, falling back to a provided dictionary."""
    return os.environ.get(key, fallback_dict.get(key))


class Config:
    """Base configuration class."""

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Explicit backend selection: DB_BACKEND=sqlite forces SQLite in-memory.
    # Default (unset or "mysql") attempts MySQL.
    _backend = (get_env_var("DB_BACKEND") or "mysql").lower()

    if _backend == "sqlite":
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    else:
        try:
            SQLALCHEMY_DATABASE_URI = (
                f"mysql+mysqlconnector://{get_env_var('DB_USER')}:{get_env_var('DB_PASSWORD')}"
                f"@{get_env_var('DB_HOST')}:{int(get_env_var('DB_PORT'))}/{get_env_var('DB_NAME')}"
            )
        except (TypeError, ValueError):
            # Safety net: fall back to SQLite if MySQL vars are misconfigured
            SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"