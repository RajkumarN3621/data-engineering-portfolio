from pathlib import Path
import pandas as pd

from data_preparation import build_assignment_candidates
from constraint_validation import validate_candidate

BASE = Path(__file__).parents[1]


def reoptimize(crew_unavailable: str):
    candidates, _ = build_assignment_candidates()
    candidates = candidates[candidates["crew_id"] != crew_unavailable]

    roster = []

    for flight_id, group in candidates.groupby("flight_id"):
        for role in ["Captain", "First Officer", "Cabin Crew"]:
            options = group[group["role"] == role]
            selected = None

            for _, row in options.sort_values("crew_id").iterrows():
                valid, _ = validate_candidate(row, 0, 0)
                if valid:
                    selected = row
                    break

            roster.append({
                "flight_id": flight_id,
                "role": role,
                "crew_id": selected["crew_id"] if selected is not None else "UNASSIGNED",
            })

    result = pd.DataFrame(roster)
    output = BASE / "output"
    output.mkdir(exist_ok=True)
    result.to_csv(output / "reoptimized_roster.csv", index=False)

    print(f"Re-optimized after unavailability of: {crew_unavailable}")
    print(result.to_string(index=False))

    return result


if __name__ == "__main__":
    reoptimize("C003")
