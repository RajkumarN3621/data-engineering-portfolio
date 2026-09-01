"""Sanitized incremental ETL example."""

import logging
from dataclasses import dataclass
from datetime import date, timedelta

import pandas as pd

from parameter_config import get_config


logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class ETLResult:
    extracted_rows: int
    transformed_rows: int
    loaded_rows: int
    status: str


def extract_source_data(start_date: date) -> pd.DataFrame:
    """Synthetic source extraction for portfolio demonstration."""
    return pd.DataFrame([
        {"customer_id": 1001, "order_date": start_date, "amount": 1200},
        {"customer_id": 1002, "order_date": start_date, "amount": 4500},
        {"customer_id": 1003, "order_date": start_date, "amount": 8000},
    ])


def transform(df: pd.DataFrame) -> pd.DataFrame:
    output = df.copy()
    output["amount"] = output["amount"].astype(float)
    output["load_date"] = pd.Timestamp.today().date()
    output["amount_band"] = output["amount"].apply(
        lambda x: "HIGH" if x >= 5000 else "STANDARD"
    )
    return output


def run(environment: str = "dev") -> ETLResult:
    config = get_config(environment)

    logger.info(
        "Starting ETL | environment=%s | target=%s.%s",
        config.environment,
        config.target_schema,
        config.target_table,
    )

    # In production this would be read from the target table.
    last_loaded_date = date.today() - timedelta(days=1)
    start_date = last_loaded_date + timedelta(days=1)

    source_df = extract_source_data(start_date)
    transformed_df = transform(source_df)

    # Portfolio mode: demonstrate the load boundary without requiring
    # access to a real Redshift cluster.
    loaded_rows = len(transformed_df)

    logger.info("Extracted rows: %s", len(source_df))
    logger.info("Transformed rows: %s", len(transformed_df))
    logger.info("Loaded rows: %s", loaded_rows)

    if len(transformed_df) != loaded_rows:
        raise RuntimeError("Source/target reconciliation failed")

    return ETLResult(
        extracted_rows=len(source_df),
        transformed_rows=len(transformed_df),
        loaded_rows=loaded_rows,
        status="SUCCESS",
    )


if __name__ == "__main__":
    print(run("dev"))
