from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineConfig:
    environment: str
    source_system: str
    target_schema: str
    target_table: str
    batch_size: int


CONFIGS = {
    "dev": PipelineConfig(
        environment="dev",
        source_system="synthetic_source",
        target_schema="analytics_dev",
        target_table="orders",
        batch_size=1000,
    ),
    "prod": PipelineConfig(
        environment="prod",
        source_system="synthetic_source",
        target_schema="analytics_prod",
        target_table="orders",
        batch_size=5000,
    ),
}


def get_config(environment: str) -> PipelineConfig:
    try:
        return CONFIGS[environment]
    except KeyError as exc:
        raise ValueError(f"Unsupported environment: {environment}") from exc
