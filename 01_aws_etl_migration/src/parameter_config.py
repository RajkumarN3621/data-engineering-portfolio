"""Environment-driven configuration for the ETL example."""

from dataclasses import dataclass


@dataclass
class PipelineConfig:
    environment: str
    database: str
    target_schema: str
    target_table: str
    staging_table: str
    notification_table: str


CONFIGS = {
    "dev": {
        "database": "analytics_dev",
        "target_schema": "curated",
        "target_table": "customer_metrics",
        "staging_table": "customer_metrics_stg",
        "notification_table": "pipeline_notifications",
    },
    "prod": {
        "database": "analytics_prod",
        "target_schema": "curated",
        "target_table": "customer_metrics",
        "staging_table": "customer_metrics_stg",
        "notification_table": "pipeline_notifications",
    },
}


def get_config(environment: str) -> PipelineConfig:
    if environment not in CONFIGS:
        raise ValueError(f"Unsupported environment: {environment}")

    return PipelineConfig(environment=environment, **CONFIGS[environment])
