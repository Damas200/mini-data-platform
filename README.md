# Mini Data Platform 

## Overview

This project implements a **Mini Data Platform** using Docker Compose.
The platform demonstrates how modern data systems ingest, process, store, and visualize data.

The system processes **sales data from CSV files**, stores the processed data in PostgreSQL, and visualizes insights using Metabase dashboards.

The platform integrates four core components:

* **MinIO** → Object storage for raw data (CSV files)
* **Apache Airflow** → Data pipeline orchestration
* **PostgreSQL** → Processed data storage
* **Metabase** → Data visualization dashboards

---

# Architecture

```
        +----------------------+
        |  Data Generator      |
        | (generate_sample_data.py)
        +-----------+----------+
                    |
                    v
              +-----------+
              |   MinIO   |
              | CSV Store |
              +-----+-----+
                    |
                    v
              +-----------+
              |  Airflow  |
              | ETL DAG   |
              +-----+-----+
                    |
                    v
             +-------------+
             | PostgreSQL  |
             | Data Store  |
             +------+------+
                    |
                    v
              +-----------+
              | Metabase  |
              | Dashboard |
              +-----------+
```

---

# Project Components

## 1️. MinIO (Object Storage)

MinIO stores raw CSV files similar to AWS S3.

Example stored file:

```
sales_data.csv
```

MinIO Console:

```
http://localhost:9001
```

---

## 2️. Apache Airflow (Data Processing)

Airflow orchestrates the ETL pipeline.

Pipeline:

```
extract → transform → load
```

Airflow UI:

```
http://localhost:8080
```

### Pipeline Tasks

**Extract**

* Download CSV file from MinIO
* Load data into a Pandas DataFrame

**Transform**

* Clean data
* Validate schema
* Format columns

**Load**

* Insert processed records into PostgreSQL

---

## 3️. PostgreSQL (Data Storage)

Processed data is stored in PostgreSQL.

Database table:

```
sales
```

Columns:

| Column      | Description             |
| ----------- | ----------------------- |
| order_id    | unique order identifier |
| customer_id | customer identifier     |
| product     | product name            |
| amount      | sales amount            |
| region      | sales region            |
| order_date  | order timestamp         |
| created_at  | ingestion timestamp     |

---

## 4️. Metabase (Visualization)

Metabase connects to PostgreSQL and provides dashboards.

Metabase UI:

```
http://localhost:3000
```

---

# Dashboard

The **Sales Analytics Dashboard** provides insights into the processed data.

Charts included:

### Total Sales

Displays overall revenue.

### Sales by Product

Bar chart showing performance of each product.

### Sales by Region

Pie chart showing geographic distribution.

### Daily Sales Trend

Line chart displaying sales growth over time.

---

# Folder Structure

```
mini-data-platform/
│
├── docker-compose.yml
├── .env
├── requirements.txt
├── README.md
│
├── dags/
│   └── sales_pipeline.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validation.py
│   └── minio_client.py
│
├── scripts/
│   └── generate_sample_data.py
│
├── data/
│   └── sales_data.csv
│
├── sql/
│   └── init_schema.sql
│
└── tests/
    └── test_transform.py
```

---

# Setup Instructions

## 1️. Clone Repository

```
git clone https://github.com/your-repo/mini-data-platform.git
cd mini-data-platform
```

---

## 2️. Start Platform

Run:

```
docker compose up -d
```

This will start:

* PostgreSQL
* Airflow
* MinIO
* Metabase

---

## 3️. Access Services

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Airflow    | [http://localhost:8080](http://localhost:8080) |
| MinIO      | [http://localhost:9001](http://localhost:9001) |
| Metabase   | [http://localhost:3000](http://localhost:3000) |
| PostgreSQL | localhost:5432                                 |

---

# Running the Data Pipeline

1️. Upload `sales_data.csv` to MinIO.

2️. Open Airflow UI:

```
http://localhost:8080
```

3️. Trigger DAG:

```
sales_etl_pipeline
```

Pipeline tasks:

```
extract → transform → load
```

---

# Example Data Flow

```
CSV file → MinIO
        ↓
Airflow extracts file
        ↓
Data is cleaned and validated
        ↓
Stored in PostgreSQL
        ↓
Metabase visualizes insights
```

---

# Testing

Unit tests validate transformation logic.

Run tests:

```
pytest
```

---

# Docker Services

Check running containers:

```
docker compose ps
```

Expected services:

```
postgres
airflow-webserver
airflow-scheduler
minio
metabase
```

---

# Screenshots

## Airflow Pipeline

```
extract → transform → load
```

## MinIO Storage

```
sales_data.csv stored in bucket
```

## Metabase Dashboard

Sales Analytics Dashboard.

---

# CI/CD Pipeline

GitHub Actions pipeline automates:

* Docker build
* Unit tests
* Data pipeline validation

Workflow file:

```
.github/workflows/pipeline.yml
```

---

# Technologies Used

* Docker
* Apache Airflow
* PostgreSQL
* MinIO
* Metabase
* Python
* Pandas
* SQLAlchemy

---

# Team Members

| Name            | Role          |
| --------------- | ------------- |
| Damas Niyonkuru | Data Engineer |

---

# Learning Outcomes

This project demonstrates:

* Building a modern **data platform**
* Designing **ETL pipelines**
* Working with **object storage**
* Managing **data warehouses**
* Creating **analytical dashboards**

---

# Conclusion

This project shows how a simple data platform can be built using open-source tools. The architecture demonstrates real-world data engineering practices including data ingestion, processing, storage, and visualization.

