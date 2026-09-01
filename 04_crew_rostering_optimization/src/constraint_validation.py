import pandas as pd


MAX_DAILY_HOURS = 8.0
MAX_DAILY_SECTORS = 4


def validate_candidate(row, assigned_hours, assigned_sectors):
    reasons = []

    if not bool(row["qualification_valid"]):
        reasons.append("qualification_invalid")

    if assigned_hours + float(row["block_hours"]) > MAX_DAILY_HOURS:
        reasons.append("daily_hours_limit")

    if assigned_sectors + 1 > MAX_DAILY_SECTORS:
        reasons.append("daily_sector_limit")

    return len(reasons) == 0, reasons


def validate_roster(roster: pd.DataFrame):
    if roster.empty:
        return {"status": "FAIL", "violations": ["empty_roster"]}

    violations = []

    assigned = roster[roster["crew_id"] != "UNASSIGNED"]

    for crew_id, group in assigned.groupby("crew_id"):
        if group["flight_id"].duplicated().any():
            violations.append(f"{crew_id}:duplicate_assignment")

        if group["block_hours"].sum() > MAX_DAILY_HOURS:
            violations.append(f"{crew_id}:daily_hours_limit")

        if len(group) > MAX_DAILY_SECTORS:
            violations.append(f"{crew_id}:daily_sector_limit")

    return {
        "status": "PASS" if not violations else "FAIL",
        "violations": violations,
    }
