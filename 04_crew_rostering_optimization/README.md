# Crew Rostering & Optimization

A sanitized portfolio implementation of a daily airline crew rostering workflow.

## Business Problem

The D-1 rostering process needs to assign Captain, First Officer, and Cabin Crew to the next day's flights while considering crew availability, qualifications, duty and rest limitations, flying hours, sectors, training, pairing rules, and operational changes.

The source POC identifies Daily Flight Plan, Monthly Crew Plan, Crew Master Data, Crew In/Out Sheet, Historical Flying Data, and Aircraft Type Data as key inputs.

## Architecture

```text
Daily Flight Plan ───────┐
Monthly Crew Plan ───────┤
Crew Master ─────────────┤
Crew In/Out ─────────────┤
Historical Flying ───────┤
Aircraft Type Data ──────┘
             |
             v
       Data Preparation
             |
             v
    Constraint Validation
             |
      +------+------+
      |             |
      v             v
 Hard Constraints  Objectives
      |             |
      +------+------+
             |
             v
      Rostering Engine
             |
             v
        D-1 Roster
             |
             v
     Operational Review
```

## Core constraint groups

The implementation separates feasibility rules from optimization objectives.

### Hard constraints

- Crew availability
- Crew role compatibility
- Aircraft qualification validity
- Duty and rest limits
- Flying-hour limits
- Sector limits
- Assignment feasibility

### Optimization objectives

After feasibility is established, assignments can be evaluated for workload balance and operational fairness.

## Data Engineering Flow

```text
Operational Inputs
        |
        v
Standardize dates / identifiers
        |
        v
Join flight + crew + qualification + availability
        |
        v
Assignment-ready dataset
        |
        v
Validate constraints
        |
        v
Generate feasible assignments
        |
        v
Select assignments
        |
        v
Publish roster
```

## D-1 Re-optimization

When crew becomes unavailable or operational inputs change, the workflow can refresh inputs and generate updated assignments.

```text
Existing Roster
      |
Operational Change
      |
      v
Refresh Inputs
      |
      v
Revalidate
      |
      v
Generate Updated Assignments
      |
      v
Updated Roster
```

## Repository Structure

```text
04_crew_rostering_optimization/
├── README.md
├── data/
│   ├── flights.csv
│   ├── crew.csv
│   ├── crew_availability.csv
│   ├── qualifications.csv
│   └── historical_flying.csv
├── src/
│   ├── data_preparation.py
│   ├── constraint_validation.py
│   ├── rostering_engine.py
│   ├── reoptimization.py
│   └── output_formatter.py
├── sql/
│   └── crew_metrics.sql
├── config/
│   └── roster_config.yaml
└── requirements.txt
```

## Run locally

```bash
cd src
python3 rostering_engine.py
python3 reoptimization.py
```

The implementation is intentionally simplified and uses synthetic data. It demonstrates the data preparation, validation, assignment, and re-optimization workflow without exposing proprietary production logic.

## Production-to-portfolio mapping

| Real-world component | Portfolio implementation |
|---|---|
| Daily flight plan | `data/flights.csv` |
| Monthly crew availability | `data/crew_availability.csv` |
| Crew master | `data/crew.csv` |
| Qualifications | `data/qualifications.csv` |
| Historical flying | `data/historical_flying.csv` |
| Data preparation | `src/data_preparation.py` |
| Constraint validation | `src/constraint_validation.py` |
| Assignment engine | `src/rostering_engine.py` |
| Re-optimization | `src/reoptimization.py` |
| Output formatting | `src/output_formatter.py` |
| Operational metrics | `sql/crew_metrics.sql` |

## Business outcome

The project was designed to automate D-1 crew scheduling, reduce manual scheduling effort, improve crew utilization, and respond faster to operational changes.

## Disclaimer

This repository contains synthetic data and a simplified portfolio implementation. It does not contain actual crew records, operational flight data, proprietary optimization code, internal rules, credentials, or confidential company information.
