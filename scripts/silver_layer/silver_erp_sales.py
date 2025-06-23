import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="data_warehouse"
)
cursor = conn.cursor()
df = pd.read_sql("SELECT * FROM bronze_crm_sales_details", conn)
df = df.dropna(subset=["sls_ord_num", "sls_prd_key", "sls_cust_id"])
date_cols = ["sls_order_dt", "sls_ship_dt", "sls_due_dt"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], unit='s', errors='coerce')
    df[col] = df[col].dt.strftime('%Y-%m-%d')
df["sls_sales"] = df["sls_sales"].fillna(0).astype(int)
df["sls_quantity"] = df["sls_quantity"].fillna(0).astype(int)
df["sls_price"] = df["sls_price"].fillna(0).astype(int)
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO silver_erp_sales_details (
            sls_ord_num, sls_prd_key, sls_cust_id,
            sls_order_dt, sls_ship_dt, sls_due_dt,
            sls_sales, sls_quantity, sls_price
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["sls_ord_num"],
        row["sls_prd_key"],
        int(row["sls_cust_id"]),
        row["sls_order_dt"],
        row["sls_ship_dt"],
        row["sls_due_dt"],
        int(row["sls_sales"]),
        int(row["sls_quantity"]),
        int(row["sls_price"])
    ))

conn.commit()
print("ERP Sales data inserted into Silver Layer.")
cursor.close()
conn.close()
