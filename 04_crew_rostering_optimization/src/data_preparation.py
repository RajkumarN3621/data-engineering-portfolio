from pathlib import Path
import pandas as pd

BASE = Path(__file__).parents[1]


def load_inputs():
    flights = pd.read_csv(BASE / "data" / "flights.csv")
    crew = pd.read_csv(BASE / "data" / "crew.csv")
    availability = pd.read_csv(BASE / "data" / "crew_availability.csv")
    qualifications = pd.read_csv(BASE / "data" / "qualifications.csv")
    history = pd.read_csv(BASE / "data" / "historical_flying.csv")

    flights["flight_date"] = pd.to_datetime(flights["flight_date"])
    flights["departure"] = pd.to_datetime(flights["departure"])
    flights["arrival"] = pd.to_datetime(flights["arrival"])
    availability["date"] = pd.to_datetime(availability["date"])
    qualifications["expiry_date"] = pd.to_datetime(qualifications["expiry_date"])

    return flights, crew, availability, qualifications, history


def build_assignment_candidates():
    flights, crew, availability, qualifications, history = load_inputs()

    available = availability.query("available == True")[["crew_id", "date"]]

    candidates = (
        flights.merge(crew, how="cross")
        .merge(
            available,
            left_on=["crew_id", "flight_date"],
            right_on=["crew_id", "date"],
            how="inner",
        )
        .merge(
            qualifications,
            on=["crew_id", "aircraft_type"],
            how="left",
        )
    )

    candidates["qualification_valid"] = (
        candidates["expiry_date"] >= candidates["flight_date"]
    )

    return candidates, history


if __name__ == "__main__":
    candidates, _ = build_assignment_candidates()
    print(f"Candidate assignments: {len(candidates)}")
