import boto3
import os

MINIO_ENDPOINT = "http://minio:9000"
ACCESS_KEY = os.getenv("MINIO_ROOT_USER")
SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD")

BUCKET_NAME = "sales-data"


def get_minio_client():
    return boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )


def download_sales_file(local_path):
    client = get_minio_client()

    client.download_file(
        BUCKET_NAME,
        "sales_data.csv",
        local_path
    )

    print("Downloaded sales_data.csv from MinIO")