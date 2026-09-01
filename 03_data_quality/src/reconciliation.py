from pathlib import Path

import pandas as pd

from validators import (
    duplicate_count,
    null_percentage,
    numeric_statistics,
    row_count,
)


def reconcile(
    source: pd.DataFrame,
    target: pd.DataFrame,
    key_columns: list[str],
    required_columns: list[str],
    numeric_columns: list[str],
) -> dict:
    source_rows = row_count(source)
    target_rows = row_count(target)

    source_nulls = null_percentage(source, required_columns)
    target_nulls = null_percentage(target, required_columns)

    source_duplicates = duplicate_count(source, key_columns)
    target_duplicates = duplicate_count(target, key_columns)

    source_stats = numeric_statistics(source, numeric_columns)
    target_stats = numeric_statistics(target, numeric_columns)

    checks = {
        "row_count_match": source_rows == target_rows,
        "target_duplicates": target_duplicates == 0,
        "target_required_columns_complete": all(
            value == 0 for value in target_nulls.values()
        ),
        "numeric_sum_match": all(
            source_stats[column]["sum"] == target_stats[column]["sum"]
            for column in numeric_columns
        ),
    }

    status = "PASS" if all(checks.values()) else "FAIL"

    return {
        "status": status,
        "checks": checks,
        "source_rows": source_rows,
        "target_rows": target_rows,
        "source_null_pct": source_nulls,
        "target_null_pct": target_nulls,
        "source_duplicates": source_duplicates,
        "target_duplicates": target_duplicates,
        "source_statistics": source_stats,
        "target_statistics": target_stats,
    }


def main():
    base = Path(__file__).parents[1]

    source = pd.read_csv(base / "sample_data" / "source_orders.csv")
    target = pd.read_csv(base / "sample_data" / "target_orders.csv")

    result = reconcile(
        source=source,
        target=target,
        key_columns=["order_id"],
        required_columns=["order_id", "customer_id", "amount"],
        numeric_columns=["amount"],
    )

    print_report(result)


def print_report(result: dict):
    print("=" * 60)
    print("DATA QUALITY RECONCILIATION REPORT")
    print("=" * 60)

    for name, value in result["checks"].items():
        print(f"{name:35} {'PASS' if value else 'FAIL'}")

    print("-" * 60)
    print(f"Source rows: {result['source_rows']}")
    print(f"Target rows: {result['target_rows']}")
    print(f"Source duplicates: {result['source_duplicates']}")
    print(f"Target duplicates: {result['target_duplicates']}")
    print(f"Overall status: {result['status']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
