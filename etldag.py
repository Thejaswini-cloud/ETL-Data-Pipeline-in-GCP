from datetime import datetime, timedelta
"""from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago"""
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
from airflow import DAG

# pylint: disable=g-import-not-at-top
try:
  from airflow.providers.standard.operators.bash import BashOperator
except ImportError:
  from airflow.operators.bash_operator import BashOperator
# pylint: enable=g-import-not-at-top

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026,2,5),
    'depends_on_past': False,
    'email': ['chittithejaswini@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py',
    )

    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="europe-southwest1 ",
    pipeline_name="etl_pipeline",
    instance_name="etl-datafusion1",
    task_id="start_datafusion_pipeline",
    )

    run_script_task >> start_pipeline
