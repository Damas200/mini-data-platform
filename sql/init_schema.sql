CREATE TABLE IF NOT EXISTS sales (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    product TEXT NOT NULL,
    amount NUMERIC CHECK (amount > 0),
    region TEXT NOT NULL,
    order_date TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);