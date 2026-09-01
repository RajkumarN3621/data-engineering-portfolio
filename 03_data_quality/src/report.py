def summarize(result: dict) -> str:
    lines = [
        f"Overall status: {result['status']}",
        f"Source rows: {result['source_rows']}",
        f"Target rows: {result['target_rows']}",
        f"Target duplicates: {result['target_duplicates']}",
    ]

    for check, passed in result["checks"].items():
        lines.append(f"{check}: {'PASS' if passed else 'FAIL'}")

    return "\n".join(lines)
