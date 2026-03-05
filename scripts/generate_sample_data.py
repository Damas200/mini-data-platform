import pandas as pd
from faker import Faker
import random

fake = Faker()

data = []

for _ in range(500):
    data.append({
        "order_id": fake.uuid4(),
        "customer_id": fake.uuid4(),
        "product": random.choice(["Laptop", "Phone", "Tablet", "Monitor"]),
        "amount": round(random.uniform(50, 2000), 2),
        "region": random.choice(["Africa", "Europe", "Asia", "America"]),
        "order_date": fake.date_between(start_date="-1y", end_date="today")
    })

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("Generated sales_data.csv")