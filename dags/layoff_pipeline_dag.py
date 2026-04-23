from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'jordan',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG(
    'layoff_pipeline',
    default_args=default_args,
    schedule_interval='@weekly',
    catchup=False
)

run_ingestion = BashOperator(
    task_id='run_ingestion',
    bash_command='python3 /Users/clerancesmal/Documents/layoff_pipeline/ingestion/load_layoffs.py',
    dag=dag
)

run_ingestion