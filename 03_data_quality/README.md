# Data Quality & Reconciliation

A sanitized portfolio project demonstrating reusable data-quality checks for ETL pipelines.

## Why this matters

A pipeline can finish successfully while the data is still wrong.

For example:

```text
Pipeline status = SUCCESS
        |
        v
Did the target receive the correct data?
        |
   +----+----+
   |         |
  YES        NO
   |         |
PASS       Investigate
```

The purpose of reconciliation is to validate the **data outcome**, not only the **pipeline execution status**.

## Validation dimensions

The framework demonstrates:

- Row-count validation
- Null / completeness checks
- Distinct-value checks
- Duplicate detection
- Numeric min / max / mean / sum checks
- Date-range validation
- Source-to-target reconciliation
- Group-level validation

The original validation utility also generated database-specific SQL for statistical checks across engines such as Teradata and SQL Server, including row counts, non-null counts, distinct counts, numeric aggregates, and date statistics. This portfolio project represents those ideas with generic SQL and pandas examples.

## Architecture

```text
                 SOURCE
                   |
                   v
             Extract / ETL
                   |
          +--------+--------+
          |                 |
          v                 v
     Source Stats       Target Stats
          |                 |
          +--------+--------+
                   |
                   v
            Reconciliation
                   |
          +--------+--------+
          |                 |
          v                 v
        PASS              FAIL
          |                 |
          v                 v
       Publish          Investigate
```

## Checks

### 1. Row count

```text
source_count == target_count
```

### 2. Completeness

Calculate the percentage of non-null values for required columns.

### 3. Uniqueness

Identify duplicate records for the business key.

### 4. Distribution / aggregate checks

Compare statistics such as:

- count
- distinct count
- min
- max
- mean
- sum

### 5. Date validation

Check that source and target processing windows align.

## Repository Structure

```text
03_data_quality/
├── src/
│   ├── validators.py
│   ├── reconciliation.py
│   └── report.py
├── sql/
│   └── data_quality_checks.sql
├── sample_data/
│   ├── source_orders.csv
│   └── target_orders.csv
└── requirements.txt
```

## Running locally

```bash
cd src
python3 reconciliation.py
```

The sample deliberately contains a data-quality issue so the framework demonstrates a failing reconciliation instead of only producing PASS results.

## Production-to-portfolio mapping

| Production pattern | Portfolio representation |
|---|---|
| Data validation utility | `src/validators.py` |
| Source/target comparison | `src/reconciliation.py` |
| Validation output | `src/report.py` |
| SQL statistics | `sql/data_quality_checks.sql` |
| Synthetic test data | `sample_data/` |

## Portfolio disclaimer

This repository uses synthetic data and generic code. It contains no client
data, credentials, internal endpoints, or proprietary production code.
