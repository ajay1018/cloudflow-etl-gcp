# ☁️ CloudFlow ETL (GCP-style, Free Tier)

Airflow-orchestrated ETL built to run locally on free tier. **Extract → Transform → (optional) Load to Postgres**, with GCP-style structure (`dags/`, `src/`, `sql/`, `data/`) and a Docker Compose quickstart. Includes sample data, schema, and a basic DAG to showcase pipeline design for Data Engineering roles.

---

## 🧱 Architecture (Mermaid)

```mermaid
flowchart TD
    A["Sources (API / CSV)"] --> B["Extract (Python)"];
    B --> C["Transform (pandas)"];
    C --> D[("PostgreSQL")];
    D --> E["Analytics / BI"];
    B -.-> F["Airflow (orchestration)"];
    C -.-> F;
    D -.-> F;
```
