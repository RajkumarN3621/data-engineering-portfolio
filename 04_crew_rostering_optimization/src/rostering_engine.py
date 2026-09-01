from pathlib import Path
import pandas as pd

from data_preparation import build_assignment_candidates
from constraint_validation import validate_candidate, validate_roster

BASE = Path(__file__).parents[1]


def generate_roster():
    candidates, _ = build_assignment_candidates()
    assignments = []
    crew_state = {}

    for flight_id, flight_group in candidates.groupby("flight_id"):
        for role in ["Captain", "First Officer", "Cabin Crew"]:
            options = flight_group[flight_group["role"] == role]

            selected = None

            for _, row in options.sort_values("crew_id").iterrows():
                state = crew_state.setdefault(
                    row["crew_id"],
                    {"hours": 0.0, "sectors": 0},
                )

                valid, _ = validate_candidate(
                    row,
                    state["hours"],
                    state["sectors"],
                )

                if valid:
                    selected = row
                    break

            if selected is None:
                assignments.append({
                    "flight_id": flight_id,
                    "flight_date": flight_group["flight_date"].iloc[0],
                    "crew_id": "UNASSIGNED",
                    "role": role,
                    "aircraft_type": flight_group["aircraft_type"].iloc[0],
                    "block_hours": 0.0,
                })
                continue

            state = crew_state[selected["crew_id"]]
            state["hours"] += float(selected["block_hours"])
            state["sectors"] += 1

            assignments.append({
                "flight_id": selected["flight_id"],
                "flight_date": selected["flight_date"],
                "crew_id": selected["crew_id"],
                "role": selected["role"],
                "aircraft_type": selected["aircraft_type"],
                "block_hours": selected["block_hours"],
            })

    roster = pd.DataFrame(assignments)

    output = BASE / "output"
    output.mkdir(exist_ok=True)
    roster.to_csv(output / "d1_roster.csv", index=False)

    validation = validate_roster(roster)

    print("D-1 roster generated")
    print(f"Assignments: {len(roster)}")
    print(f"Unassigned positions: {(roster['crew_id'] == 'UNASSIGNED').sum()}")
    print(f"Validation: {validation['status']}")

    if validation["violations"]:
        for violation in validation["violations"]:
            print(f" - {violation}")

    return roster


if __name__ == "__main__":
    generate_roster()
