from json_scraper import json_scraper
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
# from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtTestOperator


default_args = {
    "owner": "kyun",
    "depends_on_past": False,
    "start_date": datetime(2022, 1, 1),
    "email": ["kyunlee@yahoo.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}


with DAG("predictit_dag", default_args=default_args,
         schedule_interval='@daily', catchup=False) as dag:

    is_api_available = HttpSensor(
        task_id="is_api_available",
        http_conn_id="predictit_api",
        endpoint='all/'

    )

    process_json = PythonOperator(
        task_id='process_json',
        python_callable=json_scraper,
        op_kwargs={
            "url": "https://www.predictit.org/api/marketdata/all/",
            "file_name": "date.json",
            "bucket": "airflowbucketforetlproject"

        }
    )

    is_api_available >> process_json
