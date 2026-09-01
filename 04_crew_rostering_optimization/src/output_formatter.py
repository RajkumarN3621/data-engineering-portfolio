import pandas as pd


def format_roster(roster: pd.DataFrame) -> pd.DataFrame:
    return roster.sort_values(["flight_id", "role"]).reset_index(drop=True)
