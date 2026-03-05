import logging

logger = logging.getLogger(__name__)

def validate_sales(df):
    logger.info("Running data validation")

    if df.empty:
        raise ValueError("DataFrame is empty")

    if (df["amount"] <= 0).any():
        raise ValueError("Invalid amount detected")

    required_cols = {
        "order_id",
        "customer_id",
        "product",
        "amount",
        "region",
        "order_date",
    }

    if not required_cols.issubset(df.columns):
        raise ValueError("Missing required columns")

    logger.info("Validation passed")