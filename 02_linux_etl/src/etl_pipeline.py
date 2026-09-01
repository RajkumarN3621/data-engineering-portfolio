import logging
from pathlib import Path

import pandas as pd

from parameter_config import get_config
from monitoring import record_pipeline_result


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def extract(source_file: str) -> pd.DataFrame:
    logger.info("Extracting source data from %s", source_file)
    return pd.read_csv(source_file)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only fields required by the target.

    This is deliberately simple: in a real pipeline this is where business
    rules, joins, standardization, and derived fields would be applied.
    """
    output = df[["order_id", "customer_id", "order_date", "amount"]].copy()
    output["amount"] = pd.to_numeric(output["amount"], errors="coerce")
    output["order_date"] = pd.to_datetime(output["order_date"], errors="coerce")

    output = output.dropna(subset=["order_id", "customer_id", "amount"])
    output["order_value_band"] = output["amount"].apply(
        lambda x: "HIGH" if x >= 5000 else "STANDARD"
    )

    return output


def load(df: pd.DataFrame, target_file: str):
    logger.info("Loading %s rows to %s", len(df), target_file)
    Path(target_file).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(target_file, index=False)


def run(environment="dev"):
    config = get_config(environment)

    source_file = Path(__file__).parents[1] / "sample_data" / "source_orders.csv"
    target_file = Path(__file__).parents[1] / "output" / "orders_curated.csv"

    logger.info(
        "Starting %s pipeline for environment=%s",
        "orders_etl",
        config.environment,
    )

    source_df = extract(str(source_file))
    transformed_df = transform(source_df)
    load(transformed_df, str(target_file))

    record_pipeline_result(
        pipeline_name="orders_etl",
        status="SUCCESS",
        source_rows=len(source_df),
        target_rows=len(transformed_df),
    )

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run("dev")
