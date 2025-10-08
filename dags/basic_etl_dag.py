from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

def run(cmd): subprocess.check_call(cmd, shell=True)

with DAG(
    dag_id='cloudflow_basic_etl',
    start_date=datetime(2025,1,1),
    schedule_interval='@daily',
    catchup=False,
    default_args={'owner':'ajay'}
) as dag:
    extract = PythonOperator(task_id='extract', python_callable=lambda: run('python src/extract/extract_local.py'))
    transform = PythonOperator(task_id='transform', python_callable=lambda: run('python src/transform/transform_basic.py'))
    # load step requires Postgres; keep optional for now
    # load = PythonOperator(task_id='load', python_callable=lambda: run('python src/load/load_postgres.py'))
    extract >> transform  # >> load
