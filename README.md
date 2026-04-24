## Dashboard

![Layoff Analytics Dashboard](images/dashboard.png)


# Tech Layoff Analytics Pipeline

This An end-to-end data engineering and machine learning pipeline analyzing 4,357 tech layoff events from 2020–2026. Built to demonstrate production-grade pipeline architecture, three-schema warehouse design, and ML-based layoff risk classification.

## Tools & Technologies
- **Languages:** Python, SQL
- **Libraries:** pandas, scikit-learn, SQLAlchemy
- **Database:** PostgreSQL (3-schema: staging → core → mart)
- **Orchestration:** Apache Airflow
- **Containerization:** Docker
- **Visualization:** Tableau
- **ML Model:** Random Forest Classifier

## Pipeline Architecture

1. **Ingest** - Raw data laoded from csv loaded into PostgresSQL using Python

2. **Warehouse** Three schema design. Raw-> core -> Mart ->

4. **Analyze** — Tableau dashboard

5. **ML** — Random Forest classifier predicting layoff risk (AUC: 0.69)


## Key Findings

- **2023 was the worst year** — 264,320 total layoffs driven by Fed rate hikes forcing tech companies to cut after over-hiring during the 2021 zero interest rate era
- **2021 was nearly silent** — only 44 layoff events as free money flooded the market
- **Retail and Hardware hit hardest** — 106K and 95K total layoffs respectively
- **Seed stage companies average 82% laid off** — effectively full shutdowns when early stage startups fail
- **Post-IPO companies had the most events** — 1,031 events but lower severity at 17% average
- **Funds raised was the strongest ML predictor** — over-capitalized companies were most exposed to cuts when market conditions shifted
- **Oracle led single-event layoffs** — 30,000 in March 2026, the largest single event in the dataset

## How to Run

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL and run schemas in order: staging → core → mart
4. Run ingestion: `python3 ingestion/load_layoffs.py`
5. Start Airflow: `docker-compose up -d`
6. Run ML model: `python3 ml_model.py`

## Results

- Random Forest Classifier: **AUC 0.69**
- Top predictors: funds raised, country, funding stage, industry
- 4,357 layoff events analyzed across 2020–2026