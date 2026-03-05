import pandas as pd
import psycopg2
from minio_client import download_sales_file

LOCAL_FILE = "/opt/airflow/data/sales_data.csv"


def get_last_loaded_date():

    try:
        conn = psycopg2.connect(
            host="postgres",
            database="airflow",
            user="airflow",
            password="airflow"
        )

        query = "SELECT MAX(order_date) FROM sales;"
        result = pd.read_sql(query, conn)

        conn.close()

        return result.iloc[0, 0]

    except Exception:
        return None


def extract_data(file_path):

    # download latest file from MinIO
    download_sales_file(file_path)

    df = pd.read_csv(file_path)

    df["order_date"] = pd.to_datetime(df["order_date"])

    last_loaded_date = get_last_loaded_date()

    if last_loaded_date is not None:
        df = df[df["order_date"] > last_loaded_date]

    print(f"New records to process: {len(df)}")

    return df