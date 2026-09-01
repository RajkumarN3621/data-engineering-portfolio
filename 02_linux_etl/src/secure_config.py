"""Safe configuration pattern.

Secrets are intentionally supplied at runtime rather than stored in source.
"""

import os


def get_database_credentials():
    return {
        "username": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
    }


def validate_credentials(credentials):
    missing = [k for k, v in credentials.items() if not v]
    if missing:
        raise RuntimeError(
            "Missing runtime credentials: " + ", ".join(missing)
        )
