"""Sanitized Airflow DAG example.

The DAG shows orchestration responsibility only. The ETL application remains
independent and can also be executed from Linux or another scheduler.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="orders_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["portfolio", "etl"],
) as dag:

    run_etl = BashOperator(
        task_id="run_python_etl",
        bash_command=(
            "cd /opt/etl/02_linux_etl/src && "
            "python3 etl_pipeline.py"
        ),
    )
