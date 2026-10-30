<p align="center">
  <img src="header.svg" alt="Sagar Konkanagaon: an animated end-to-end data platform that detects schema drift and heals itself" width="100%"/>
</p>

### Hi, I'm Sagar 👋

I build data platforms end to end, from the first byte ingested to the dashboard, API or AI model
that uses it, and I make them **notice when they break, and fix themselves**.
Five years of Spark, Databricks, Delta Lake, Airflow and BigQuery across e-commerce,
automotive, finance and industrial IoT. Most recently at eBay, migrating 300+ production pipelines.

- 🏭 **[The Data Foundry](https://data-foundry-sand.vercel.app)**: watch a live pipeline run, break it on purpose, and see it heal
- 🧪 **[spark-pipeline-labs](https://github.com/sagarkonkanagaon-netizenk/spark-pipeline-labs)**: production patterns (streaming dedup, SCD2, skew salting, idempotent backfills) as tested PySpark + Delta code
- 📓 **[til](https://github.com/sagarkonkanagaon-netizenk/til)**: short notes on what I learn each week

### 🗺️ The whole data engineering lifecycle

```mermaid
flowchart LR
  subgraph IN[Ingest]
    A1[Batch & APIs]
    A2[Streaming events]
    A3[CDC from databases]
  end
  subgraph ST[Store]
    B1[(Data lake / lakehouse)]
    B2[(Warehouse)]
  end
  subgraph TR[Transform & model]
    C1[Clean · dedup · conform]
    C2[Dimensional models · SCD2]
  end
  subgraph SV[Serve]
    D1[BI & dashboards]
    D2[APIs & reverse ETL]
    D3[ML features · RAG]
  end
  IN --> ST --> TR --> SV
  GOV{{Governance · quality · lineage · security}} -.-> ST & TR & SV
  OPS{{Orchestration · CI/CD · observability · cost}} -.-> IN & TR
```

| Stage | What I care about |
|---|---|
| **Ingestion** | Batch loads, REST/API pulls, Kafka-style event streams and database CDC, with late and duplicate data handled on purpose |
| **Storage** | Lakehouse (Delta Lake) and warehouse (BigQuery) designs, file formats, partitioning, compaction and retention |
| **Processing** | Spark batch and Structured Streaming, SQL, incremental and exactly-once patterns, skew and shuffle tuning |
| **Data modeling** | Star schemas, facts and dimensions, SCD Type 2, layered models (raw, conformed, business) that people can trust |
| **Orchestration** | Airflow DAGs with retries, SLAs, backfills and deferrable sensors; event-driven runs where batch is too slow |
| **Data quality** | Contracts and tests at every boundary, freshness/volume/schema checks, quarantine instead of silent corruption |
| **Governance & security** | Catalogs, lineage, access control, PII masking, auditability |
| **Serving** | BI-ready marts, semantic layers, APIs and reverse ETL, ML feature tables |
| **DataOps** | Everything as code: Git, CI on every PR, Docker, tested pipelines, safe deploys and rollbacks |
| **Cost & performance** | Right-sized clusters, pruning, caching, Z-ordering, and knowing what each query costs |

### 🏛️ Architecture principles

- **Replayable by design**: raw data is kept, every step can be re-run, every write is idempotent
- **Fail loudly, heal quietly**: bad data is stopped at the edge, and known failures repair themselves
- **Batch and streaming, one model**: the same logic serves both, so numbers agree
- **Built for the next reader**: documented tables, clear ownership, lineage you can follow

### ☁️ Cloud-native implementation

- **Compute:** Databricks and Spark clusters that autoscale, serverless SQL where it fits
- **Storage:** cloud object storage with Delta Lake tables, BigQuery for analytics
- **Platform:** containers, infrastructure as code, secrets and access managed centrally
- **Delivery:** CI/CD for pipelines like any other software, with tests before anything touches prod

### 🤖 AI on top of the data

- **LLM apps on real data:** The Data Foundry's "Ask the Engine" chat answers questions with retrieval (BM25) over curated content
- **AI-ready data:** clean, documented tables that feed ML features and RAG instead of a pile of CSVs
- **AI for operations:** pipelines that detect drift and anomalies and repair themselves

### 🧰 Toolbox

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4169E1?logo=postgresql&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?logo=databricks&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD4?logo=delta&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?logo=apachekafka&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?logo=apacheairflow&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?logo=googlebigquery&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

**Currently:** open to Senior Data Engineer roles ·
[LinkedIn](https://www.linkedin.com/in/sagar-konkanagaon-346914156) ·
[sagarkonkanagaon@gmail.com](mailto:sagarkonkanagaon@gmail.com)
