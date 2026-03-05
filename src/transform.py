import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting transformation")

    df = df.dropna()
    df["amount"] = df["amount"].astype(float)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df.drop_duplicates(subset=["order_id"])

    logger.info(f"After cleaning: {len(df)} rows")
    return df