import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.transform import transform_sales
import pandas as pd


def test_transform_sales():

    data = {
        "order_id": ["1"],
        "customer_id": ["C1"],
        "product": ["Laptop"],
        "amount": [1000],
        "region": ["Africa"],
        "order_date": ["2024-01-01"]
    }

    df = pd.DataFrame(data)

    result = transform_sales(df)

    assert not result.empty
    assert "amount" in result.columns