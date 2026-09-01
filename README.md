# Data Engineering Portfolio

Practical, sanitized examples covering AWS data migration, Python ETL, SQL, data quality, performance optimization, orchestration, and crew optimization.

## Projects

### 01. AWS ETL Migration & Modernization

Modernized a legacy Linux-based ETL pattern into an AWS architecture using S3, Redshift, Athena, SageMaker Processing, Step Functions, EventBridge, Secrets Manager, and CloudWatch.

Key patterns:

- Active vs inactive dataset migration
- Incremental ETL
- Parameter-driven environments
- Staging and curated layers
- Source-to-target reconciliation
- Managed processing with SageMaker
- Step Functions orchestration
- Secure secret management
- Centralized logging and monitoring
- Chunked data loading and performance optimization

### 02. Linux ETL

Python and SQL based ETL patterns for integrating data from multiple relational source systems.

### 03. Data Quality

Reusable validation patterns for row counts, nulls, duplicates, aggregates, and source-to-target reconciliation.

### 04. Crew Rostering & Optimization

Constraint-driven workforce planning and crew scheduling using optimization techniques.

## Repository Structure

```text
data-engineering-portfolio/
│
├── 01_aws_etl_migration/
│   ├── architecture/
│   ├── orchestration/
│   ├── sql/
│   └── src/
│
├── 02_linux_etl/
├── 03_data_quality/
├── 04_crew_optimization/
│
├── .gitignore
└── README.md
```

## Portfolio Disclaimer

This repository is a sanitized portfolio implementation. It does not contain production credentials, client data, private endpoints, AWS account IDs, internal database names, or proprietary production code.
