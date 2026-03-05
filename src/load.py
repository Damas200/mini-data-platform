import pandas as pd
from sqlalchemy import create_engine, text

DB_URI = "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"

def load_data(df: pd.DataFrame):

    if df.empty:
        print("No new data to load.")
        return

    engine = create_engine(DB_URI)

    with engine.begin() as conn:

        # get existing order_ids
        existing = pd.read_sql(
            text("SELECT order_id FROM sales"),
            conn
        )

        # filter new rows only
        df = df[~df["order_id"].isin(existing["order_id"])]

        if df.empty:
            print("No new rows to insert.")
            return

        df.to_sql(
            "sales",
            conn,
            if_exists="append",
            index=False,
            method="multi"
        )

    print(f"{len(df)} new records inserted.")