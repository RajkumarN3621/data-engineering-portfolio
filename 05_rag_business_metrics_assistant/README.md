# RAG Business Metrics Assistant

A backend-focused RAG data pipeline for turning business metric documentation into a searchable, structured knowledge base.

This project intentionally does **not** include a web frontend, chatbot UI, application deployment, or company-specific infrastructure. The focus is on the data engineering and retrieval pipeline.

## Problem

Enterprise metric definitions are often spread across large volumes of documentation. Analysts need a reliable way to retrieve:

- Metric definitions
- Business meaning
- Calculation formulas
- Dimensions and filters
- Related documentation
- Relevant context for downstream SQL or analytics workflows

The portfolio pipeline converts source documentation into retrieval-ready knowledge.

## Architecture

```text
Business Documentation
        |
        v
Document Ingestion
        |
        v
Cleaning & Normalization
        |
        v
Chunking
        |
        v
Metadata Enrichment
        |
        v
Embedding Generation
        |
        v
Vector Index (FAISS)
        |
        v
Retriever
        |
        v
Relevant Context
        |
        +-------------------+
        |                   |
        v                   v
Metric Context        Optional SQL Context
        |                   |
        +---------+---------+
                  |
                  v
             LLM Layer
          (Llama / DeepSeek)
                  |
                  v
        Grounded Response
```

## Data Engineering Focus

The core pipeline is:

```text
Raw documentation
       ↓
Parse
       ↓
Clean
       ↓
Chunk
       ↓
Attach metadata
       ↓
Create embeddings
       ↓
Build vector index
       ↓
Persist index + metadata
       ↓
Retrieve relevant chunks
```

This is the part that matters most from a Data Engineering perspective: the LLM is downstream of a well-structured ingestion and retrieval layer.

## Components

| Component | Purpose |
|---|---|
| Document loader | Reads supported documentation files |
| Cleaner | Normalizes text before indexing |
| Chunker | Splits documents into retrieval-sized units |
| Metadata builder | Preserves metric/source information |
| Embedding layer | Converts text into vectors |
| FAISS index | Performs similarity search |
| Retriever | Returns relevant context |
| Prompt builder | Constrains LLM input to retrieved context |
| LLM adapter | Supports Llama / DeepSeek-style generation |

## Repository Structure

```text
05_rag_business_metrics_assistant/
├── README.md
├── src/
│   ├── document_loader.py
│   ├── text_processing.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── pipeline.py
├── data/
│   └── sample_metrics/
│       ├── revenue.md
│       ├── active_customers.md
│       └── conversion_rate.md
├── config/
│   └── pipeline_config.example.json
├── scripts/
│   └── build_index.py
└── requirements.txt
```

## Example retrieval flow

A question such as:

```text
What is the definition and formula for conversion rate?
```

is handled as:

```text
Question
  ↓
Embedding
  ↓
FAISS similarity search
  ↓
Top relevant metric chunks
  ↓
Metadata + context
  ↓
LLM prompt
  ↓
Grounded answer
```

The LLM should answer from retrieved context rather than inventing a metric definition.

## Running locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the sample index:

```bash
python3 scripts/build_index.py
```

Run retrieval:

```bash
python3 -m src.pipeline "What is the conversion rate formula?"
```

The example uses a deterministic local TF-IDF vector representation so the repository can be executed without API keys or model downloads. The production architecture can replace this adapter with the embedding and LLM models used in the original implementation.

## Production mapping

The original project involved processing a large body of metric documentation and building document ingestion and retrieval pipelines using LangChain, FAISS, Llama, and DeepSeek. The resume describes support for 100+ business metrics and processing/chunking/indexing of business documentation. 

This repository intentionally represents the same **engineering pattern** with synthetic documentation and replaceable model adapters.

## What this project demonstrates

- RAG data pipeline design
- Document ingestion
- Text preprocessing
- Chunking strategy
- Metadata management
- Embedding/vector search concepts
- FAISS indexing
- Retrieval pipelines
- LLM context construction
- Grounded generation
- Separation of data pipeline and model layer
- Reproducible local execution

## Security

No API keys, credentials, production documents, internal URLs, or proprietary content are included.
