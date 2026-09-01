from datetime import datetime


def record_pipeline_result(
    pipeline_name: str,
    status: str,
    source_rows: int,
    target_rows: int,
):
    reconciliation_status = "PASS" if source_rows == target_rows else "FAIL"

    result = {
        "pipeline_name": pipeline_name,
        "status": status,
        "source_rows": source_rows,
        "target_rows": target_rows,
        "reconciliation_status": reconciliation_status,
        "timestamp": datetime.utcnow().isoformat(),
    }

    print(result)
    return result
