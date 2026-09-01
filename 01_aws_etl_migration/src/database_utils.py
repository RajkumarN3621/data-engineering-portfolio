"""Database access abstraction.

Production credentials are intentionally not hard-coded.
Use an approved connector and secret-management mechanism at runtime.
"""

from dataclasses import dataclass
import os


@dataclass
class DatabaseConfig:
    host: str
    database: str
    user: str
    password: str
    port: int = 5439


class DatabaseClient:
    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.connection = None

    def connect(self):
        if not self.config.host:
            raise ValueError("Database host is required")

        # Replace with the approved Redshift connector in a real deployment.
        print(f"Connecting to {self.config.database}:{self.config.port}")
        return self

    def execute(self, query: str):
        if not query.strip():
            raise ValueError("Query cannot be empty")

        print(f"Executing SQL: {query[:120]}...")
        return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None


def database_config_from_env() -> DatabaseConfig:
    return DatabaseConfig(
        host=os.environ.get("DB_HOST", ""),
        database=os.environ.get("DB_NAME", ""),
        user=os.environ.get("DB_USER", ""),
        password=os.environ.get("DB_PASSWORD", ""),
        port=int(os.environ.get("DB_PORT", "5439")),
    )
