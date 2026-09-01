# Linux ETL Engineering

A sanitized portfolio project demonstrating a multi-source ETL pattern using Python, SQL, Linux execution, Airflow-style orchestration, and Alteryx-style workflow scheduling.

## Business Problem

Data was available across multiple relational systems such as Teradata, Oracle, and SQL Server. The ETL layer needed to:

- Extract data from different source systems
- Apply business transformations
- Load curated data into a target warehouse
- Run reliably on a schedule
- Handle environment-specific parameters
- Provide logging and operational visibility
- Reconcile source and target results

Two orchestration patterns are represented:

```text
                 +-------------------+
                 | Source Systems     |
                 | Teradata           |
                 | Oracle             |
                 | SQL Server         |
                 +---------+---------+
                           |
                           v
                    Python / SQL ETL
                           |
                 +---------+---------+
                 |                   |
                 v                   v
            Linux + Airflow     Alteryx Workflow
                 |                   |
                 v                   v
             Scheduled          Gallery Schedule
                 |                   |
                 +---------+---------+
                           |
                           v
                    Target Warehouse
```

## Engineering Patterns

### 1. Parameter-driven execution

The same pipeline can run against different environments without changing the ETL code.

### 2. Secure credentials

Credentials are not hard-coded. The example uses environment variables and a secret-provider abstraction.

### 3. Incremental processing

The pipeline determines the processing boundary and extracts only the required data rather than repeatedly processing the full dataset.

### 4. Monitoring and reconciliation

A successful workflow execution does not automatically mean the target is correct. The project demonstrates operational checks such as:

- Pipeline status
- Source row count
- Target row count
- Duplicate checks
- Maximum load date
- Validation status

### 5. Performance optimization

The portfolio example demonstrates how unnecessary columns and redundant transformations increase processing cost. Removing work that does not contribute to the final target reduces pipeline runtime.

A representative production scenario involved optimizing a workflow estate with many workflows and staging tables by removing unused columns and unnecessary transformations.

## Repository Structure

```text
02_linux_etl/
├── src/
│   ├── etl_pipeline.py
│   ├── parameter_config.py
│   ├── database_client.py
│   ├── monitoring.py
│   └── secure_config.py
├── orchestration/
│   └── airflow_dag.py
├── sql/
│   └── reconciliation.sql
├── config/
│   └── pipeline_config.example.json
├── sample_data/
│   └── source_orders.csv
└── requirements.txt
```

## Running locally

```bash
cd src
python3 etl_pipeline.py
```

This portfolio version uses synthetic data and does not connect to production systems.

## Production-to-portfolio mapping

| Production pattern | Portfolio representation |
|---|---|
| Linux Python ETL | `src/etl_pipeline.py` |
| Environment parameters | `src/parameter_config.py` |
| Database utility layer | `src/database_client.py` |
| Credential protection | `src/secure_config.py` |
| Airflow scheduling | `orchestration/airflow_dag.py` |
| Monitoring | `src/monitoring.py` |
| Reconciliation | `sql/reconciliation.sql` |
| Performance optimization | README + transformation design |

## Disclaimer

This repository contains sanitized examples and synthetic data. It does not contain client data, credentials, internal endpoints, production table names, or proprietary production code.
