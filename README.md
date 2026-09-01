# Data Engineering Portfolio

Practical projects across **data engineering**, **cloud migration**, **data quality**, **optimization**, **RAG**, and **GenAI analytics**.

Focus: reliable pipelines, modernizing legacy workloads, validating outcomes (not just job status), improving performance, and production-oriented GenAI data workflows.

---

## Contents

| # | Project | Focus |
|---|---------|--------|
| 01 | [AWS ETL Migration & Modernization](./01_aws_etl_migration) | Legacy → AWS architecture |
| 02 | [Linux ETL Engineering](./02_linux_etl) | Multi-source ETL on Linux |
| 03 | [Data Quality & Reconciliation](./03_data_quality) | Validate pipeline *data*, not only runs |
| 04 | [Crew Rostering & Optimization](./04_crew_rostering_optimization) | Assignment-ready data + re-opt |
| 05 | [RAG Business Metrics Assistant](./05_rag_business_metrics_assistant) | Docs → retrieval-ready knowledge base |
| 06 | [GenAI Claims Analytics](./06_genai_claims_analytics) | Metric change → drivers → explanation |

---

## Projects

### 01 · AWS ETL Migration & Modernization

Modernized legacy Linux ETL into an AWS-oriented processing architecture.

**Highlights**

- Legacy-to-cloud migration (active and inactive datasets)
- Storage & query: **S3**, **Redshift**, **Athena**
- Compute & orchestration: **Python ETL**, **SageMaker Processing**, **Step Functions**, **EventBridge**
- Ops: **Secrets Manager**, **CloudWatch**
- Incremental loads, source-to-target reconciliation, performance & cost tuning

→ [View project](./01_aws_etl_migration)

---

### 02 · Linux ETL Engineering

Multi-source ETL with Python, SQL, Linux execution, and workflow orchestration.

**Highlights**

- Sources: **Teradata**, **Oracle**, **SQL Server**
- Execution: Python/SQL on Linux, **Airflow**, **Alteryx** (+ Gallery scheduling)
- Parameter-driven runs, secure credentials, monitoring
- Incremental processing, reconciliation, ETL performance optimization

→ [View project](./02_linux_etl)

---

### 03 · Data Quality & Reconciliation

Reusable framework to validate **ETL outcomes**, not only pipeline success.

**Highlights**

- Row counts, nulls/completeness, distinct counts, duplicates
- Numeric aggregates (min / max / mean / sum)
- Date-range checks and reconciliation reporting
- SQL-based quality rules

> **Core idea:** Pipeline success ≠ data success.

→ [View project](./03_data_quality)

---

### 04 · Crew Rostering & Optimization

Data prep and optimization workflow for daily crew rostering and operational re-optimization.

**Highlights**

- Flight schedule, crew master, availability, qualifications
- Historical flying data and constraint validation
- Assignment-ready datasets, D-1 roster generation
- Operational re-optimization; workload & assignment analysis

→ [View project](./04_crew_rostering_optimization)

---

### 05 · RAG Business Metrics Assistant

Backend-focused RAG pipeline: business docs → searchable, retrieval-ready knowledge base.

**Highlights**

- Ingestion → clean/normalize → chunk → metadata
- Embeddings, vector index, **FAISS** similarity search
- Semantic retrieval, context construction, LLM answers
- Grounded responses for metric definitions and formulas

Retrieval/data pipeline is separated from the model layer.

→ [View project](./05_rag_business_metrics_assistant)

---

### 06 · GenAI Claims Analytics

GenAI workflow to explain metric changes and surface the drivers behind them.

**Highlights**

- Period comparison (current vs prior)
- Analysis by business unit, market, and store
- Driver decomposition and quantified impact
- Automated explanations and decision-support insights

**Flow**

```text
Business Metric
      ↓
Current vs Prior Period
      ↓
Calculate Change
      ↓
Identify Key Drivers
      ↓
Quantify Driver Impact
      ↓
Generate Explanation
      ↓
Business-ready Insight
```

→ [View project](./06_genai_claims_analytics)

---

## Technology Stack

| Area | Tools |
|------|--------|
| **Languages** | Python, SQL, Bash |
| **AWS** | S3, Redshift, Athena, Step Functions, SageMaker, EventBridge, Secrets Manager, CloudWatch |
| **Data engineering** | Spark / PySpark, Airflow, Alteryx, ETL/ELT, data quality & reconciliation, incremental processing |
| **GenAI** | LangChain, FAISS, embeddings, RAG, Llama, DeepSeek |
| **Analytics & optimization** | Pandas, NumPy, constraint-based optimization, driver & business-metric analysis |

---

## Engineering Focus

| Theme | Principle |
|-------|-----------|
| **Reliable pipelines** | Success status is not enough — validate, reconcile, monitor, and fail clearly. |
| **Cloud migration** | Separate storage, compute, orchestration, security, and monitoring. |
| **Performance** | Prefer incremental loads, lean columns, and fewer unnecessary transforms. |
| **Data quality** | Catch “job succeeded, data wrong” with source-to-target checks. |
| **Optimization** | Clean, validated inputs before constraints and objectives. |
| **GenAI foundations** | Ingestion, chunking, metadata, embeddings, and retrieval matter as much as the model. |

---

## Repository Structure

```text
data-engineering-portfolio/
├── 01_aws_etl_migration/
├── 02_linux_etl/
├── 03_data_quality/
├── 04_crew_rostering_optimization/
├── 05_rag_business_metrics_assistant/
├── 06_genai_claims_analytics/
├── .gitignore
└── README.md
```

---

## Portfolio Scope

These are **sanitized portfolio implementations** that demonstrate engineering patterns.

Excluded on purpose: production credentials, customer data, internal endpoints, account IDs, proprietary datasets, and confidential business information.

Where production used enterprise-specific infra, models, or data, these projects use generic configs and synthetic/sample data to show the approach.
