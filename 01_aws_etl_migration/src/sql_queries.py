"""Reusable SQL templates for incremental ETL."""


def max_loaded_date(schema: str, table: str) -> str:
    return f"""
        SELECT MAX(load_date) AS max_load_date
        FROM {schema}.{table}
    """


def delete_staging(schema: str, table: str) -> str:
    return f"DELETE FROM {schema}.{table}"


def count_rows(schema: str, table: str) -> str:
    return f"SELECT COUNT(*) AS row_count FROM {schema}.{table}"


def insert_target(schema: str, staging_table: str, target_table: str) -> str:
    return f"""
        INSERT INTO {schema}.{target_table}
        SELECT *
        FROM {schema}.{staging_table}
    """
