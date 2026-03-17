from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
from io import StringIO

sys.path.append("/opt/airflow/src")

from extract import extract_data
from transform import transform_sales as transform_sales_data
from load import load_data


DATA_FILE = "/opt/airflow/data/sales_data.csv"


def run_extract(**context):
    df = extract_data(DATA_FILE)
    context["ti"].xcom_push(key="extracted_data", value=df.to_json())


def run_transform(**context):
    import pandas as pd

    df_json = context["ti"].xcom_pull(key="extracted_data")

    df = pd.read_json(StringIO(df_json))

    # apply transformation
    df = transform_sales_data(df)

    context["ti"].xcom_push(key="transformed_sales", value=df.to_json())


def run_load(**context):
    import pandas as pd

    df_json = context["ti"].xcom_pull(key="transformed_sales")

    df = pd.read_json(StringIO(df_json))

    load_data(df)


with DAG(
    dag_id="sales_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task